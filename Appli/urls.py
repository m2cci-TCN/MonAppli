from django.urls import path

from Appli import views
#ici tous les chemins sont accompagnés de Application/ car définis dans MonAppli.urls
urlpatterns = [
    path('Acceuil/', views.acceuil, name="Application-Acceuil"),
    path('Page-<str:numeropage>/', views.page, name="Application-pages"), #Variable de type string : numeropage #Quand on appelle le chemin finissant par page-01, 01 est récupéré pour être passé en argument de numeropage
]
