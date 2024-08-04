"""
    Ce fichier permet de créer le fond d'un niveau
    à l'aide des listes Ligne1, Ligne2, ...
"""

#importation des bibliothèques
from constante import*
import pygame
from pygame.locals import *
pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))

#Chargement des images pour le fond
mur=pygame.image.load(image_mur).convert_alpha()
mur=pygame.transform.scale(mur,(taille_sprite,taille_sprite))

herbe=pygame.image.load(image_herbe).convert()
herbe=pygame.transform.scale(herbe,(taille_sprite,taille_sprite))

eau=pygame.image.load(image_eau).convert()
eau=pygame.transform.scale(eau,(taille_sprite,taille_sprite))

chateau=pygame.image.load(image_chateau).convert()
chateau=pygame.transform.scale(chateau,(taille_sprite,taille_sprite))

#Création des lignes du fond
Ligne0=list('mmmmmmmmmmmmmmmmmmmm')
Ligne1=list('mHHmHHmHHHmmmmmmHHHm')
Ligne2=list('mHHmHmmHmHmHHHHHHmmmm')
Ligne3=list('mHHHHHHHmHmHHmHHEmHm')
Ligne4=list('mmmmmmmHmHmHmmmmmmHm')
Ligne5=list('mEEHHHmHmHHHHmHHHHHm')
Ligne6=list('mEHHHHHHmHHHHmHHHEEm')
Ligne7=list('mEHHHmHHmEEmHHHmmmmm')
Ligne8=list('mHHmmmmmmmmmHHHmHHHm')
Ligne9=list('mHHHHHHHHHHHHHHmHmHm')
Ligne10=list('mHHmmmmmmmHHmmmmHmHm')
Ligne11=list('mHHmHHHHHmHHmHHHHmHm')
Ligne12=list('mHHmHmmmmmHHmmmmmmHm')
Ligne13=list('mHHmHHHHHHHHHHHHHHHm')
Ligne14=list('mmmmmmmmmmmmmmmmmmmm')
#Ligne14=['m' for i in range(0,nbr_sprite_longueur)]  ## que des murs

L=[Ligne0,Ligne1,Ligne2,Ligne3,Ligne4,Ligne5,Ligne6,Ligne7,Ligne8,Ligne9,Ligne10,\
Ligne11,Ligne12,Ligne13,Ligne14]

def fond_niveau(L):
    numero_ligne=0
    for ligne in L:
        numero_case=0
        #parcours de la ième Ligne
        for sprite in ligne:
            x=numero_case*taille_sprite
            y=numero_ligne*taille_sprite
            if sprite=="E" :
                fenetre.blit(eau,(x,y))
            elif sprite=="m" :
                fenetre.blit(mur,(x,y))
            else :
                fenetre.blit(herbe,(x,y))
            numero_case=numero_case+1
        numero_ligne=numero_ligne+1
    pygame.image.save(fenetre,'images/niveau.bmp')