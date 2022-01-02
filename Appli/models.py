# Create your models here.
from django.db import models
from django.utils.text import slugify


class Societe(models.Model):
    nom = models.CharField(max_length=50, primary_key=True)
    taille = models.IntegerField()
    localisation = models.CharField(max_length=50)
    type = models.CharField(max_length=20)



class Experiences(models.Model):
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE)
    rang = models.CharField(max_length=30)
    slug = models.SlugField()
    publish = models.BooleanField(default=False)
    annee = models.DateField(null=True)
    time = models.IntegerField(blank=False)
    desc = models.TextField()

    def EstVisualisable(self):
        if (self.publish):
            return "L'experience est visualisable"
        return "L'experience n'est pas visualisable"

    def slugging(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.rang)

    def save(self, *args,
             **kwargs):  # Avec la méthode save on peut désormais mettre à jour l'entrée ajoutée comme prévu initialement mais en plus de cela le champs slug est renseigné.
        if not self.slug:
            self.slug = slugify(self.rang)

        super().save(*args, **kwargs)


### RELATION PLUSIEURS A UN

## Pour ajouter une societé et une experiences dans une de ces société, la primari key de Societe est son nom, la clé étrangere d'Experience vers les société également.

# from Appli.models import Experiences, Societe

## Creation de la societe ATEAU
# post = Societe.objects.create(nom="ATEAU", taille = 20, localisation = "Grenoble", type = "SCOP")

## Creation d'une experience chez la societe ATEAU, le champs societé correspond à l'objet dans la table societé dont la PK est ATEAU
# post = Experiences.objects.create(societe= Societe.objects.get(pk = "ATEAU"), rang="Technicien Cartographe",publish=1, annee='2020-10-01', time=13, desc="Blablabla")



###RELATION PLUSIEURS A PLUSIEUR :





# post = Experiences(id=1, societe="IRSTEA", rang="Stagiaire Télédétection",
#                    publish=1, annee='2019-05-01', time=5, ville="Grenoble", desc="Blablabla")
# post.save()  ## Méthode de base qui permet de mettre à jour le champs.
#
# # Méthode 2 d'ajout d'entrée dans la BDD :
# #
# post = Experiences.objects.create(id=2, societe="ATEAU", rang="Technicien Cartographe",
#                                   publish=1, annee='2020-10-01', time=13, ville="Grenoble", desc="Blablabla")
#
# # # Selection de toutes les entities
# Selection = Experiences.objects.all()
#
# # # Selection précise des entitées où societe = ATEAU
# Selection = Experiences.objects.get(societe="ATEAU")
#
# #  Selections des entitées ou le rang = Technicien cartographe (Renvoi un QuerySet : une collection d'objet)
# Selections = Experiences.objects.filter(rang="Technicien Cartographe")
#
# # # # Selections de la premiere entitée ou le rang = Technicien cartographe
# # Selection = Experiences.objects.filter(rang="Technicien Cartographe").first()
# #
# # # #Selections des entitée ou rang = Technicien cartographe et societe = ATEAU
# # Selections = Experiences.objects.filter(rang="Technicien Cartographe", societe="ATEAU")
# #
# # # Selection par filtre :
# # Selections = Experiences.objects.filter(annee__year="2020")
# #
# # # Récupérer tous les articles qui contiennent le mot Technicien dans le rang (sensible à la casse) :
# # Selections = Experiences.objects.filter(rang__contains="Technicien")
# #
# # # Récupérer tous les articles qui contiennent le mot Technicien dans le rang (insensible à la casse) :
# # Selections = Experiences.objects.filter(rang__icontains="Technicien")
# #
# # # Récupérer tous les articles qui comment par le mot Python (sensible à la casse) :
# # Selections = Experiences.objects.filter(rang__startswith="Technicien")
# #
# # # Pour ordonner un QuerySet selon un champ, on utilise la méthode order_by :
# #
# # Experiences.objects.order_by('annee')
# # Experiences.objects.order_by('-annee')  # on peut inverser le sens en mettant - devant le nom du champ
# # # Il n'est pas obligatoire de préciser all. Par défaut, si vous ne mettez pas all, toutes les entrées de la base de données seront retournées. Il est donc redondant d'écrire BlogPost.objects.all().order_by('date').
# #
# # # Selection des entitée dont le rang contient Technicien, triée par la date.
# # Experiences.objects.filter(rang__icontains="Technicien").order_by('annee')
# #
# # # Pour récupérer seulement une partie d'un QuerySet, on peut utiliser les slices natifs de Python. Par exemple pour récupérer seulement les trois premiers articles de blog :
# #
# # Experiences.objects.all()[:3]
# #
# # # Pour MODIFIER des entréé :
# # post = Experiences.objects.get(societe="ATEAU")
# # post.desc = "Cartographie - Arpentage - CATEC"
# # post.save()
# #
# # # Pour Supprimer : (à ne pas lancer ici mais dans un shell plutot
# #
# # # if Experiences.objects.get(societe="ATEAU") is not None:
# # #     Experiences.objects.get(societe="ATEAU").delete()
# # #
# #
# # # posts = BlogPost.objects.all()
# # # posts.delete()
# # # Supprimer un article en particulier :
# # #
# # # post = BlogPost.objects.get(title="Un article plus trop super")
# # # post.delete()
