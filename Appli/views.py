from datetime import datetime

from django.shortcuts import render


# Create your views here.

def ouverture(request):
    return render(request, "ouverture.html")

def acceuil(request):
    return render(request, "Acceuil.html", context={"DATE": datetime.today()})


#Pour rendre plus dynamique l'appel de plusieurs pages (Page-01, Page-02, Page-03) en passant par une seule view
def page(request, numeropage):
    if numeropage in ["01", "02", "03"]:
        return render(request, f"Page-{numeropage}.html") #On utilise la variable numeropage définie dans urls.py
    else:
        return render (request , "NotFound.html", context={"NUM": numeropage}) #Si l'argument numero page n'est pas éxistant dans les noms de pages déjà existantes,
                                                                                # alors on redirige vers une page d'erreur, on peut même lui passer en paramètre le numéro
                                                                                    # demandé dans la requete qui n'est pas reconnu