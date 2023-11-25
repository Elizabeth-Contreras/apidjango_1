"""API9ISC22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import Home
from api.views import Pag2
from api.views import Inicio
from api.views import Recupera, Ejemplo, Contacto, Chat
from api.views import ingresa_usuario, Informar,Calendario
from api.views import login_view, grafica

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', Home.as_view(), name='index'),
    path('registro.html', Pag2.as_view(), name='registro'),
    path('principal.html', Inicio.as_view(), name='principal'),
    path('ejemplos.html', Ejemplo.as_view(), name='ejemplos'),
    path('contacto.html', Contacto.as_view(), name='contacto'),
    path('informar.html', Informar.as_view(), name='informar'),
    path('calendario.html', Calendario.as_view(), name='calendario'),
    path('chat.html', Chat.as_view(), name='chat'),
    path('recuperar.html', Recupera.as_view(), name='recuperar'), 
    path('registro/', ingresa_usuario, name='ingresa_usuario'),
    #path('admin/', admin.site.urls),
    path('index/', login_view, name='login_view'),

]