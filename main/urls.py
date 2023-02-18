from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_graph/', views.render_graph1, name='get_graph'),
    path('estocastico/', views.render_estocastico, name='estocastico'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('cursos-gratuitos/', views.cursos_gratuitos, name='cursos-gratuitos'),
    path('mentoria/', views.mentoria, name='mentoria'),
    path('predicoes/', views.predicoes, name='predicoes'),
    path('analise-de-carteira/', views.analise_de_carteira, name='analise-de-carteira'),
    path('ferramentas/', views.ferramentas, name='ferramentas'),
    path('raio-x-do-mercado/', views.raio_x_do_mercado, name='raio-x-do-mercado'),
    path('form-graph1/', views.form_graph1, name='form-graph1'),
    path('simples/', views.render_simples, name='simples'),
    path('form-estocastico/', views.form_estocastico, name='form-estocastico'),
]