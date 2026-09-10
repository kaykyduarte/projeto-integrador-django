from django.urls import path
from . import views

urlpatterns = [
    path('exibir_grafico/', views.exibir_grafico),
]