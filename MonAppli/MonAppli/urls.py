"""MonAppli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from MonAppli import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ouverture, name="Acceuil"),
    path('Acceuil/', views.acceuil, name="Application-Acceuil"),
    path('Page-<str:numeropage>/', views.page, name="Application-pages"),
    # Variable de type string : numeropage #Quand on appelle le chemin finissant par page-01, 01 est récupéré pour être passé en argument de numeropage
]
