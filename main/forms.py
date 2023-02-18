from django import forms

YEAR = ['2019' ,'2020', '2021', '2022', '2023']


class SimpleForm(forms.Form):
    inicio = forms.DateField(widget=forms.SelectDateWidget(years=YEAR))
    fim = forms.DateField(widget=forms.SelectDateWidget(years=YEAR))
    tickrate = forms.IntegerField(max_value=22, required=True)
    BVSP = forms.BooleanField(required=False)
    PETR4 = forms.BooleanField(required=False)
    ITUB4 = forms.BooleanField(required=False)
    VALE3 = forms.BooleanField(required=False)
    BBDC4 = forms.BooleanField(required=False)
    BBAS3 = forms.BooleanField(required=False)
    OIBR3 = forms.BooleanField(required=False)
    ALUP11 = forms.BooleanField(required=False)
    IRBR3 = forms.BooleanField(required=False)
    TRPL4 = forms.BooleanField(required=False)
    BMGB4 = forms.BooleanField(required=False)
    ENAT3 = forms.BooleanField(required=False)
    WEGE3 = forms.BooleanField(required=False)
    PSSA3 = forms.BooleanField(required=False)
    LUPA3 = forms.BooleanField(required=False)