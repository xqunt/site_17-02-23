from django.shortcuts import render
from . import utils
from .forms import SimpleForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Postagem

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def cursos_gratuitos(request):
    return render(request, 'cursos-gratuitos.html')

def mentoria(request):
    return render(request, 'mentoria.html')

def predicoes(request):
    return render(request, 'predicoes.html')

def analise_de_carteira(request):
    return render(request, 'analise-de-carteira.html')

def ferramentas(request):
    return render(request, 'ferramentas.html')

def raio_x_do_mercado(request):
    return render(request, 'raio-x-do-mercado.html')

def render_graph1(request):
    context = {
    'graphs': utils.get_graph(request),
}
    return render(request, 'graph.html', context)

def form_graph1(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SimpleForm()

    return render(request, 'form-graph1.html', {'form': form})

def render_estocastico(request):
    context = {
        'graphs': utils.estocastico(),
    }
    return render(request, 'estocastico.html', context)

def form_estocastico(request):
    
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SimpleForm()
    return render(request, 'form-estocastico.html', {'form': form})

def render_simples(request):
    context = {
        'graphs': utils.simples(request),
    }
    return render(request, 'simples.html', context)

def blog(request):
    posts = Postagem.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)

def unit_blog(request):
    post = Postagem.objects.filter(id__name='')