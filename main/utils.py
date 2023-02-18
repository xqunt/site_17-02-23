import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mplfinance as fplt
from pandas_datareader import data as pdr
from datetime import date
import ta
import yfinance as yf
import warnings
from io import BytesIO
import base64
from . import utils
from .forms import SimpleForm
from datetime import date



def low_level():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph







def get_graph(request):
    form = SimpleForm(request.POST)

    yf.pdr_override()
    warnings.filterwarnings("ignore")
    tickers = ["^BVSP", "PETR4.SA", "ITUB4.SA", "VALE3.SA"
           , "BBDC4.SA", "BBAS3.SA", "OIBR3.SA", "ALUP11.SA"
           , "IRBR3.SA", "TRPL4.SA", "BMGB4.SA", "ENAT3.SA"
           , "WEGE3.SA", "PSSA3.SA", "LUPA3.SA"]

    day_inicio = form.data['inicio_day']
    if day_inicio == "1" or "2" or "3" or "4" or "5" or "6" or "7"or "8" or "9":
        day_inicio = f"0{day_inicio}"
    month_inicio = form.data['inicio_month']
    if month_inicio == "1" or "2" or "3" or "4" or "5" or "6" or "7"or "8" or "9":
        month_inicio = f"0{month_inicio}"

    day_fim = form.data['fim_day']
    if day_fim == "1" or "2" or "3" or "4" or "5" or "6" or "7"or "8" or "9":
        day_fim = f"0{day_fim}"
    month_fim = form.data['fim_month']
    if month_fim == "1" or "2" or "3" or "4" or "5" or "6" or "7"or "8" or "9":
        month_fim = f"0{month_fim}"

    inicio = str(f"{form.data['inicio_year']}-{month_inicio}-{day_inicio}")

    fim = str(f"{form.data['fim_year']}-{month_fim}-{day_fim}")

    if inicio and fim:
        ibov = pdr.get_data_yahoo(tickers, start = inicio, end = fim)
    df_mapa = ibov["Adj Close"][tickers]
    df_mapa.rename(columns = {"^BVSP": "BVSP_Close", "PETR4.SA": "PETR_Close", "ITUB4.SA": "ITUB_Close"
                            , "VALE3.SA": "VALE_Close", "BBDC4.SA": "BBDC_Close", "BBAS3.SA": "BBAS_Close"
                            , "OIBR3.SA": "OIBR_Close", "ALUP11.SA": "ALUP_Close", "IRBR3.SA": "IRBR_Close"
                            , "TRPL4.SA": "TRPL_Close", "BMGB4.SA": "BMGB_Close", "ENAT3.SA": "ENAT_Close"
                            , "WEGE3.SA": "WEGE_Close", "PSSA3.SA": "PSSA_Close", "LUPA3.SA": "LUPA_Close"}, inplace = True)
    p = int(form.data['tickrate'])
    df_mapa["MM_bvsp"] = df_mapa["BVSP_Close"].rolling(p).mean()
    df_mapa["MM_petro"] = df_mapa["PETR_Close"].rolling(p).mean()
    df_mapa["MM_itub"] = df_mapa["ITUB_Close"].rolling(p).mean()
    df_mapa["MM_vale"] = df_mapa["VALE_Close"].rolling(p).mean()
    df_mapa["MM_bbdc"] = df_mapa["BBDC_Close"].rolling(p).mean()
    df_mapa["MM_bbas"] = df_mapa["BBAS_Close"].rolling(p).mean()
    df_mapa["MM_oibr"] = df_mapa["OIBR_Close"].rolling(p).mean()
    df_mapa["MM_alup"] = df_mapa["ALUP_Close"].rolling(p).mean()
    df_mapa["MM_irbr"] = df_mapa["IRBR_Close"].rolling(p).mean()
    df_mapa["MM_trpl"] = df_mapa["TRPL_Close"].rolling(p).mean()
    df_mapa["MM_bmgb"] = df_mapa["BMGB_Close"].rolling(p).mean()
    df_mapa["MM_enat"] = df_mapa["ENAT_Close"].rolling(p).mean()
    df_mapa["MM_WEGE"] = df_mapa["WEGE_Close"].rolling(p).mean()
    df_mapa["MM_pssa"] = df_mapa["PSSA_Close"].rolling(p).mean()
    df_mapa["MM_lupa"] = df_mapa["LUPA_Close"].rolling(p).mean()
    df_mapa["RSL_BVSP"] = (df_mapa["BVSP_Close"]/df_mapa["MM_bvsp"] - 1)*100
    df_mapa["RSL_PETR"] = (df_mapa["PETR_Close"]/df_mapa["MM_petro"] - 1)*100
    df_mapa["RSL_ITUB"] = (df_mapa["ITUB_Close"]/df_mapa["MM_itub"] - 1)*100
    df_mapa["RSL_VALE"] = (df_mapa["VALE_Close"]/df_mapa["MM_vale"] - 1)*100
    df_mapa["RSL_BBDC"] = (df_mapa["BBDC_Close"]/df_mapa["MM_bbdc"] - 1)*100
    df_mapa["RSL_BBAS"] = (df_mapa["BBAS_Close"]/df_mapa["MM_bbas"] - 1)*100
    df_mapa["RSL_OIBR"] = (df_mapa["OIBR_Close"]/df_mapa["MM_oibr"] - 1)*100
    df_mapa["RSL_ALUP"] = (df_mapa["ALUP_Close"]/df_mapa["MM_alup"] - 1)*100
    df_mapa["RSL_IRBR"] = (df_mapa["IRBR_Close"]/df_mapa["MM_irbr"] - 1)*100
    df_mapa["RSL_TRPL"] = (df_mapa["TRPL_Close"]/df_mapa["MM_trpl"] - 1)*100
    df_mapa["RSL_BMGB"] = (df_mapa["BMGB_Close"]/df_mapa["MM_bmgb"] - 1)*100
    df_mapa["RSL_ENAT"] = (df_mapa["ENAT_Close"]/df_mapa["MM_enat"] - 1)*100
    df_mapa["RSL_WEGE"] = (df_mapa["WEGE_Close"]/df_mapa["MM_WEGE"] - 1)*100
    df_mapa["RSL_PSSA"] = (df_mapa["PSSA_Close"]/df_mapa["MM_pssa"] - 1)*100
    df_mapa["RSL_LUPA"] = (df_mapa["LUPA_Close"]/df_mapa["MM_lupa"] - 1)*100
    bvsp_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["BVSP_Close"], window = 2)
    bvsp_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["BVSP_Close"], window = 14)
    petr_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["PETR_Close"], window = 2)
    petr_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["PETR_Close"], window = 14)
    itub_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["ITUB_Close"], window = 2)
    itub_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["ITUB_Close"], window = 14)
    vale_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["VALE_Close"], window = 2)
    vale_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["VALE_Close"], window = 14)
    bbdc_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["BBDC_Close"], window = 2)
    bbdc_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["BBDC_Close"], window = 14)
    bbas_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["BBAS_Close"], window = 2)
    bbas_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["BBAS_Close"], window = 14)

    oibr_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["OIBR_Close"], window = 2)
    oibr_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["OIBR_Close"], window = 14)

    alup_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["ALUP_Close"], window = 2)
    alup_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["ALUP_Close"], window = 14)

    irbr_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["IRBR_Close"], window = 2)
    irbr_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["IRBR_Close"], window = 14)

    trpl_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["TRPL_Close"], window = 2)
    trpl_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["TRPL_Close"], window = 14)

    bmgb_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["BMGB_Close"], window = 2)
    bmgb_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["BMGB_Close"], window = 14)

    enat_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["ENAT_Close"], window = 2)
    enat_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["ENAT_Close"], window = 14)

    WEGE_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["WEGE_Close"], window = 2)
    WEGE_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["WEGE_Close"], window = 14)

    pssa_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["PSSA_Close"], window = 2)
    pssa_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["PSSA_Close"], window = 14)

    lupa_rsi2 = ta.momentum.RSIIndicator(close = df_mapa["LUPA_Close"], window = 2)
    lupa_rsi14 = ta.momentum.RSIIndicator(close = df_mapa["LUPA_Close"], window = 14)


    df_mapa["RSI2_PETR"] = petr_rsi2.rsi()
    df_mapa["RSI14_PETR"] = petr_rsi14.rsi()

    df_mapa["RSI2_BVSP"] = bvsp_rsi2.rsi()
    df_mapa["RSI14_BVSP"] = bvsp_rsi14.rsi()

    df_mapa["RSI2_ITUB"] = itub_rsi2.rsi()
    df_mapa["RSI14_ITUB"] = itub_rsi14.rsi()

    df_mapa["RSI2_VALE"] = vale_rsi2.rsi()
    df_mapa["RSI14_VALE"] = vale_rsi14.rsi()

    df_mapa["RSI2_BBDC"] = bbdc_rsi2.rsi()
    df_mapa["RSI14_BBDC"] = bbdc_rsi14.rsi()

    df_mapa["RSI2_BBAS"] = bbas_rsi2.rsi()
    df_mapa["RSI14_BBAS"] = bbas_rsi14.rsi()

    df_mapa["RSI2_OIBR"] = oibr_rsi2.rsi() 
    df_mapa["RSI14_OIBR"] = oibr_rsi14.rsi() 

    df_mapa["RSI2_ALUP"] = alup_rsi2.rsi() 
    df_mapa["RSI14_ALUP"] = alup_rsi14.rsi() 

    df_mapa["RSI2_IRBR"] = irbr_rsi2.rsi() 
    df_mapa["RSI14_IRBR"] = irbr_rsi14.rsi() 

    df_mapa["RSI2_TRPL"] = trpl_rsi2.rsi() 
    df_mapa["RSI14_TRPL"] = trpl_rsi14.rsi()

    df_mapa["RSI2_BMGB"] = bmgb_rsi2.rsi() 
    df_mapa["RSI14_BMGB"] = bmgb_rsi14.rsi()

    df_mapa["RSI2_ENAT"] = enat_rsi2.rsi() 
    df_mapa["RSI14_ENAT"] = enat_rsi14.rsi() 

    df_mapa["RSI2_WEGE"] = WEGE_rsi2.rsi() 
    df_mapa["RSI14_WEGE"] = WEGE_rsi14.rsi() 

    df_mapa["RSI2_PSSA"] = pssa_rsi2.rsi() 
    df_mapa["RSI14_PSSA"] = pssa_rsi14.rsi() 

    df_mapa["RSI2_LUPA"] = lupa_rsi2.rsi() 
    df_mapa["RSI14_LUPA"] = lupa_rsi14.rsi()

    indicadores = []
    
    BVSP = form['BVSP'].value()
    PETR4 = form['PETR4'].value()
    ITUB4 = form['ITUB4'].value()
    VALE3 = form['VALE3'].value()
    BBDC4 = form['BBDC4'].value()
    BBAS3 = form['BBAS3'].value()
    OIBR3 = form['OIBR3'].value()
    ALUP11 = form['ALUP11'].value()
    IRBR3 = form['IRBR3'].value()
    TRPL4 = form['TRPL4'].value()
    BMGB4 = form['BMGB4'].value()
    ENAT3 = form['ENAT3'].value()
    WEGE3 = form['WEGE3'].value()
    PSSA3 = form['PSSA3'].value()
    LUPA3 = form['LUPA3'].value()


    if BVSP:
        indicadores.append(["BVSP", df_mapa["RSL_BVSP"].tail(1)[0], df_mapa["RSI14_BVSP"].tail(1)[0]])
    if PETR4:
        indicadores.append(["PETR4", df_mapa["RSL_PETR"].tail(1)[0], df_mapa["RSI14_PETR"].tail(1)[0]])
    if ITUB4:
        indicadores.append(["ITUB4", df_mapa["RSL_ITUB"].tail(1)[0], df_mapa["RSI14_ITUB"].tail(1)[0]])
    if VALE3:
        indicadores.append(["VALE3", df_mapa["RSL_VALE"].tail(1)[0], df_mapa["RSI14_VALE"].tail(1)[0]])
    if BBDC4:
        indicadores.append(["BBDC4", df_mapa["RSL_BBDC"].tail(1)[0], df_mapa["RSI14_BBDC"].tail(1)[0]])
    if BBAS3:
        indicadores.append(["BBAS3", df_mapa["RSL_BBAS"].tail(1)[0], df_mapa["RSI14_BBAS"].tail(1)[0]])
    if OIBR3:
        indicadores.append(["OIBR3", df_mapa["RSL_OIBR"].tail(1)[0], df_mapa["RSI14_OIBR"].tail(1)[0]])
    if ALUP11:
        indicadores.append(["ALUP11", df_mapa["RSL_ALUP"].tail(1)[0], df_mapa["RSI14_ALUP"].tail(1)[0]])
    if IRBR3:
        indicadores.append(["IRBR3", df_mapa["RSL_IRBR"].tail(1)[0], df_mapa["RSI14_IRBR"].tail(1)[0]])
    if TRPL4:
        indicadores.append(["TRPL4", df_mapa["RSL_TRPL"].tail(1)[0], df_mapa["RSI14_TRPL"].tail(1)[0]])
    if BMGB4:
        indicadores.append(["BMGB4", df_mapa["RSL_BMGB"].tail(1)[0], df_mapa["RSI14_BMGB"].tail(1)[0]])
    if ENAT3:
        indicadores.append(["ENAT3", df_mapa["RSL_ENAT"].tail(1)[0], df_mapa["RSI14_ENAT"].tail(1)[0]])
    if WEGE3:
        indicadores.append(["WEGE3", df_mapa["RSL_WEGE"].tail(1)[0], df_mapa["RSI14_WEGE"].tail(1)[0]])
    if PSSA3:
        indicadores.append(["PSSA3", df_mapa["RSL_PSSA"].tail(1)[0], df_mapa["RSI14_PSSA"].tail(1)[0]])
    if LUPA3:
        indicadores.append(["LUPA3", df_mapa["RSL_LUPA"].tail(1)[0], df_mapa["RSI14_LUPA"].tail(1)[0]])

    mapa = pd.DataFrame(indicadores, columns = ["Ativo", "RSL", "RSI14"])
    
    # GRAPHS

    plt.plot(df_mapa["RSL_PETR"], df_mapa["RSI2_PETR"], ".", color = "blue")
    plt.title("PETR4 - RSL(10) e RSI(2)")
    plt.plot(df_mapa["RSL_PETR"], df_mapa["RSI14_PETR"], ".", color = "blue")
    plt.title("PETR4 - RSL(10) e RSI(14)")
    plt.plot(df_mapa["RSL_BVSP"], df_mapa["RSI2_BVSP"], ".", color = "green")
    plt.title("ibovespa - RSL(10) e RSI(2)")
    plt.plot(df_mapa["RSL_BBAS"], df_mapa["RSI14_BBAS"], "x", color = "green")
    plt.title("BBAS3 - RSL(10) e RSI(14)")
    plt.figure(figsize = (18, 10))
    plt.scatter(mapa["RSL"], mapa["RSI14"], s = 80)
    for i in range(mapa.shape[0]):
        plt.text(x = mapa.RSL[i] + 0.6, y = mapa.RSI14[i] + 0.6 , s = mapa.Ativo[i], 
                fontdict = dict(color = "white", size = 14),
                bbox = dict(facecolor = "black", alpha = 0.7))

    plt.xlim(mapa.RSL.min() - 1, mapa.RSL.max() + 5)               
    plt.ylim(mapa.RSI14.min() - 2, mapa.RSI14.max() + 4)          

    setup = dict(size = 13, color = "black")
    plt.text(8, 50, "Show me the money", **setup)
    d0 = date(int(form.data['inicio_year']), int(month_inicio), int(day_inicio))
    d1 = date(int(form.data['fim_year']), int(month_fim), int(day_fim))
    delta = d1 - d0
    plt.title(f"Mapa do Indice Força Relativa ({str(delta.days)} dias)  e Distância da Média Móvel de ({p} dias) - {fim}") 
    plt.xlabel(f"RSL({p}) em %")                        
    plt.ylabel(f"RSI({str(delta.days)})")                     
    #plt.show()
    graph = utils.low_level()
    return graph

def estocastico():
    tickers = "JHSF3.SA"
    start = "2022-10-01"
    end = "2023-01-05"

    df = yf.download(tickers, start= start, end=end).copy()[["High", "Low", "Adj Close"]]
    n = 8 
    n_highest_high = df["High"].rolling(n).max()
    n_lowest_low = df["Low"].rolling(n).min()
    df["%K"] = (
        (df["Adj Close"] - n_lowest_low) / 
        (n_highest_high - n_lowest_low)
    ) * 100
    df["%D"] = df['%K'].rolling(3).mean()
    df.dropna(inplace=True)
    df["Slow %K"] = df["%D"]
    df["Slow %D"] = df["Slow %K"].rolling(3).mean()
    plt.axhline(y=20.0, color='black', linestyle='--', linewidth=1)
    plt.axhline(y=80.0, color='black', linestyle='--', linewidth=1)
    plt.ylim(0, 100.0)
    fig, (ax1, ax2) = plt.subplots(
        nrows=2, 
        sharex=True,
        figsize=(20,8), 
        gridspec_kw={"height_ratios": [3, 1]})

    ax1.plot(df.index, df["Adj Close"], label="Fechamento")
    ax1.legend()

    ax2.plot(df.index, df[["Slow %K"]], label='Estocástico Lento')
    ax2.plot(df.index, df[["Slow %D"]], label='MMA(3)', linewidth=1)
    ax2.axhline(y=80, color='black', linestyle='--', linewidth=1)
    ax2.axhline(y=20, color='black', linestyle='--', linewidth=1)
    ax2.set_ylim(0, 100)
    ax2.legend()
    graph = utils.low_level()
    return graph

def simples(request):
    inicio = '2020-01-01'
    fim = '2023-02-16'
    vale = yf.download('VALE3.SA', start = inicio, 
                   end = fim)
    vale[['Adj Close']].plot(figsize = (10,10))
    graph = utils.low_level()
    return graph


