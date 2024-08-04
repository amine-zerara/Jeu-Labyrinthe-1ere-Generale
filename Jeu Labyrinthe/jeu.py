# Importation des bibliothèques
from constante import*
from creation_fond_niveau import*
import pygame
from pygame.locals import *
pygame.init()

            # Chargement des images

# Chargement et affichage de l'image du niveau
fond_niveau(L)
image_niveau = "images/niveau.bmp"
fond_niveau = pygame.image.load(image_niveau).convert_alpha()
fenetre.blit(fond_niveau,(0,0))


# Affichage Chevalier
perso=pygame.image.load(image_perso).convert_alpha()
perso=pygame.transform.scale(perso,(taille_sprite,taille_sprite)) # Redimensionner l'image
perso_arme=pygame.image.load(image_perso_arme).convert_alpha()
perso_arme=pygame.transform.scale(perso_arme,(taille_sprite,taille_sprite))
arme=pygame.image.load(image_arme).convert_alpha()
arme=pygame.transform.scale(arme,(taille_sprite,taille_sprite))
potion_pv=pygame.image.load(image_potion_pv).convert_alpha()
potion_pv=pygame.transform.scale(potion_pv,(taille_sprite,taille_sprite))
bouton=pygame.image.load(image_bouton).convert_alpha()
bouton=pygame.transform.scale(bouton,(taille_sprite,taille_sprite))
mur_casse=pygame.image.load(image_mur_casse).convert_alpha()
mur_casse=pygame.transform.scale(mur_casse,(taille_sprite,taille_sprite))
piece1=pygame.image.load(image_piece1).convert_alpha()
piece1=pygame.transform.scale(piece1,(taille_sprite,taille_sprite))
piece2=pygame.image.load(image_piece2).convert_alpha()
piece2=pygame.transform.scale(piece2,(taille_sprite,taille_sprite))
piece3=pygame.image.load(image_piece3).convert_alpha()
piece3=pygame.transform.scale(piece3,(taille_sprite,taille_sprite))
clef1=pygame.image.load(image_clef1).convert_alpha()
clef1=pygame.transform.scale(clef1,(taille_sprite,taille_sprite))
clef2=pygame.image.load(image_clef2).convert_alpha()
clef2=pygame.transform.scale(clef2,(taille_sprite,taille_sprite))
chateau=pygame.image.load(image_chateau).convert_alpha()
chateau=pygame.transform.scale(chateau,(taille_sprite,taille_sprite))
mechant=pygame.image.load(image_mechant).convert_alpha()
mechant=pygame.transform.scale(mechant,(taille_sprite,taille_sprite))
herbe=pygame.image.load(image_herbe).convert_alpha()
herbe=pygame.transform.scale(herbe,(taille_sprite,taille_sprite))
eau1=pygame.image.load(image_eau).convert_alpha()
eau1=pygame.transform.scale(eau1,(taille_sprite,taille_sprite))
eau2=pygame.image.load(image_eau).convert_alpha()
eau2=pygame.transform.scale(eau2,(taille_sprite,taille_sprite))
eau3=pygame.image.load(image_eau).convert_alpha()
eau3=pygame.transform.scale(eau3,(taille_sprite,taille_sprite))
eau4=pygame.image.load(image_eau).convert_alpha()
eau4=pygame.transform.scale(eau4,(taille_sprite,taille_sprite))
eau5=pygame.image.load(image_eau).convert_alpha()
eau5=pygame.transform.scale(eau5,(taille_sprite,taille_sprite))
eau6=pygame.image.load(image_eau).convert_alpha()
eau6=pygame.transform.scale(eau6,(taille_sprite,taille_sprite))
eau7=pygame.image.load(image_eau).convert_alpha()
eau7=pygame.transform.scale(eau7,(taille_sprite,taille_sprite))
eau8=pygame.image.load(image_eau).convert_alpha()
eau8=pygame.transform.scale(eau8,(taille_sprite,taille_sprite))
eau9=pygame.image.load(image_eau).convert_alpha()
eau9=pygame.transform.scale(eau9,(taille_sprite,taille_sprite))


# Préparation au déplacement perso
position_perso=perso.get_rect() # Coordonnée du perso
position_perso=position_perso.move(taille_sprite,taille_sprite)
fenetre.blit(perso,position_perso)
pygame.display.flip()

            # Boucle principale infinie de jeu


def affiche_objets_init(L):
    fenetre.blit(arme,(taille_sprite*5,taille_sprite*3))
    L[3][5]='arme'
    fenetre.blit(bouton,(taille_sprite*18,taille_sprite*1))
    L[1][18]='bouton'
    fenetre.blit(potion_pv,(taille_sprite*11,taille_sprite*2))
    L[2][11]='potion_pv'
    fenetre.blit(mur_casse,(taille_sprite*4,taille_sprite*2))
    L[2][4]='mur_casse'
    fenetre.blit(piece1,(taille_sprite*5,taille_sprite*5))
    L[5][5]='piece1'
    fenetre.blit(piece2,(taille_sprite*18,taille_sprite*3))
    L[3][18]='piece2'
    fenetre.blit(piece3,(taille_sprite*8,taille_sprite*11))
    L[11][8]='piece3'
    fenetre.blit(clef1,(taille_sprite*4,taille_sprite*1))
    L[1][4]='clef1'
    fenetre.blit(clef2,(taille_sprite*1,taille_sprite*13))
    L[13][1]='clef2'
    fenetre.blit(chateau,(taille_sprite*13,taille_sprite*11))
    L[11][13]='chateau'
    fenetre.blit(mechant,(taille_sprite*7,taille_sprite*4))
    L[4][7]='mechant'
    fenetre.blit(herbe,(taille_sprite*16,taille_sprite*10))
    L[10][16]='herbe'
    fenetre.blit(eau1,(taille_sprite*2,taille_sprite*5))
    L[5][2]='eau1'
    fenetre.blit(eau1,(taille_sprite*1,taille_sprite*5))
    L[5][1]='eau2'
    fenetre.blit(eau1,(taille_sprite*1,taille_sprite*6))
    L[6][1]='eau3'
    fenetre.blit(eau1,(taille_sprite*1,taille_sprite*7))
    L[7][1]='eau4'
    fenetre.blit(eau1,(taille_sprite*9,taille_sprite*7))
    L[7][9]='eau5'
    fenetre.blit(eau1,(taille_sprite*10,taille_sprite*7))
    L[7][10]='eau6'
    fenetre.blit(eau1,(taille_sprite*16,taille_sprite*3))
    L[3][16]='eau7'
    fenetre.blit(eau1,(taille_sprite*17,taille_sprite*6))
    L[6][17]='eau8'
    fenetre.blit(eau1,(taille_sprite*18,taille_sprite*6))
    L[6][18]='eau9'


def affiche_objets(liste_objets):
    if 'arme' in liste_objets:
        fenetre.blit(arme,(taille_sprite*5,taille_sprite*3))
    if 'bouton' in liste_objets:
        fenetre.blit(bouton,(taille_sprite*18,taille_sprite*1))
    if 'potion_pv' in liste_objets:
        fenetre.blit(potion_pv,(taille_sprite*11,taille_sprite*2))
    if 'mur_casse' in liste_objets:
        fenetre.blit(mur_casse,(taille_sprite*4,taille_sprite*2))
    if 'piece1' in liste_objets:
        fenetre.blit(piece1,(taille_sprite*5,taille_sprite*5))
    if 'piece2' in liste_objets:
        fenetre.blit(piece2,(taille_sprite*18,taille_sprite*3))
    if 'piece3' in liste_objets:
        fenetre.blit(piece3,(taille_sprite*8,taille_sprite*11))
    if 'clef1' in liste_objets:
        fenetre.blit(clef1,(taille_sprite*4,taille_sprite*1))
    if 'clef2' in liste_objets:
        fenetre.blit(clef2,(taille_sprite*1,taille_sprite*13))
    if 'chateau' in liste_objets:
        fenetre.blit(chateau,(taille_sprite*13,taille_sprite*11))
    if 'mechant' in liste_objets:
        fenetre.blit(mechant,(taille_sprite*7,taille_sprite*4))
    if 'herbe' in liste_objets:
        fenetre.blit(herbe,(taille_sprite*16,taille_sprite*10))
    if 'eau1' in liste_objets:
        fenetre.blit(eau1,(taille_sprite*2,taille_sprite*5))
    if 'eau2' in liste_objets:
        fenetre.blit(eau2,(taille_sprite*1,taille_sprite*5))
    if 'eau3' in liste_objets:
        fenetre.blit(eau3,(taille_sprite*1,taille_sprite*6))
    if 'eau4' in liste_objets:
        fenetre.blit(eau4,(taille_sprite*1,taille_sprite*7))
    if 'eau5' in liste_objets:
        fenetre.blit(eau5,(taille_sprite*9,taille_sprite*7))
    if 'eau6' in liste_objets:
        fenetre.blit(eau6,(taille_sprite*10,taille_sprite*7))
    if 'eau7' in liste_objets:
        fenetre.blit(eau7,(taille_sprite*16,taille_sprite*3))
    if 'eau8' in liste_objets:
        fenetre.blit(eau8,(taille_sprite*17,taille_sprite*6))
    if 'eau9' in liste_objets:
        fenetre.blit(eau9,(taille_sprite*18,taille_sprite*6))

def ramassage_piece(ligne,colonne):
    pieces=["piece1","piece2","piece3"] # Liste des pièces
    if L[ligne][colonne] in pieces : # Si je suis dans une case avec une pièce
        liste_objets.remove(L[ligne][colonne]) # Suppression de la pièce dans la liste-objets
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        return True
    return False

def ramassage_clef(ligne,colonne):
    clefs=["clef1","clef2"] # Liste des clefs
    if L[ligne][colonne] in clefs : # Si je suis dans une case avec une clef
        liste_objets.remove(L[ligne][colonne]) # Suppression de la clef dans la liste-objets
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        return True
    return False

def potion_recupere(ligne,colonne):
    potion_liste=["potion_pv"] # Liste de la potion
    if L[ligne][colonne] in potion_liste and PV<=5: # Si je suis dans une case avec une potion
        liste_objets.remove(L[ligne][colonne]) # Suppression de la potion dans la liste-objet
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        return True
    return False

def arme_recupere(ligne,colonne):
    arme=["arme"] # Liste de l'arme
    if L[ligne][colonne] in arme : # Si je suis dans une case avec une arme
        liste_objets.remove(L[ligne][colonne]) # Suppression de l'arme dans la liste-objet
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        return True
    return False

def bouton_recupere(ligne,colonne):
    bouton_liste=["bouton"] # Liste de la bouton
    if L[ligne][colonne] in bouton_liste : # Si je suis dans une case avec une bouton
        liste_objets.remove(L[ligne][colonne]) # Suppression de la bouton dans la liste-objet
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        L[2][4]='H'
        return True
    return False

def casse_mur(ligne,colonne):
    mur_liste=["mur_casse"] # Liste du mur
    if L[ligne][colonne] in mur_liste and compteur_bouton==1 : # Si je suis dans une case avec un mur
        liste_objets.remove(L[ligne][colonne]) # Suppression du mur dans la liste-objet
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        return True
    return False

def ennemi_tue(ligne,colonne):
    ennemi=["mechant"] # Liste du méchant
    if L[ligne][colonne] in ennemi : # Si je suis dans une case avec un méchant
        liste_objets.remove(L[ligne][colonne]) # Suppression du méchant dans la liste-objet
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        return True
    return False

def herbe_cache(ligne,colonne):
    herbe_list=["herbe"]
    if compteur_clefs==2 and compteur_pieces==3:
        if L[ligne][colonne] in herbe_list :
            liste_objets.remove(L[ligne][colonne])
            L[10][16]='H'
            return True
    return False

def temple_mur(ligne,colonne):
    passage=["mur"] # Liste du mur
    if L[ligne][colonne] in mur and compteur_pieces==1 or compteur_clefs==1: # Si je suis dans une case avec le temple et que j'ai au moins une clef
        liste_objets.remove(L[ligne][colonne]) # Suppression du mur dans la liste-objet
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        return True
    return False

def temple_recup(ligne,colonne):
    temple=["chateau"] # Liste du temple
    if L[ligne][colonne] in temple and compteur_clefs==2 and compteur_pieces==3: # Si je suis dans une case avec le temple et que j'ai les 2 clefs et les 3 pièces
        liste_objets.remove(L[ligne][colonne]) # Suppression du temple dans la liste-objet
        L[ligne][colonne]='H' # On remet de l'herbe dans la matrice L
        return True
    return False

def marche_eau(ligne,colonne):
    eau_liste=["eau1","eau2","eau3","eau4","eau5","eau6","eau7","eau8","eau9"] # Liste de l'eau
    if L[ligne][colonne] in eau_liste : # Si je suis dans une case avec de l'eau
        L[ligne][colonne]='eau*' # On remet de l'eau dans la matrice L
        return True
    return False

print("PV : 10")
# i=1 et j=1 -> position initiale du chevalier
i=1 # Numéro ligne
j=1 # Numéro colonne
affiche_objets_init(L)
liste_objets = ["arme","bouton","potion_pv","mur_casse","piece1","piece2","piece3","clef1","clef2","chateau","mechant","herbe","eau1","eau2","eau3","eau4","eau5","eau6","eau7","eau8","eau9"]
compteur_pieces=0
compteur_clefs=0
compteur_ennemis=0
compteur_herbe=0
compteur_temple=0
compteur_bouton=0
PV=10
gagner=False
perdu=False
continuer=True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
            if event.key == K_DOWN: # Si "flèche bas"
                if L[i+1][j]!='m':
                    position_perso = position_perso.move(0,taille_sprite)
                    i=i+1
            if event.key == K_UP: # Si "flèche haut"
                if L[i-1][j]!='m' and L[i-1][j]!='mur_casse':
                    position_perso = position_perso.move(0,-taille_sprite)
                    i=i-1
            if event.key == K_LEFT: # Si "flèche gauche"
                if L[i][j-1]!='m':
                    position_perso = position_perso.move(-taille_sprite,0)
                    j=j-1
            if event.key == K_RIGHT: # Si "flèche droite"
                if L[i][j+1]!='m':
                    position_perso = position_perso.move(taille_sprite,0)
                    j=j+1


    # Ramasser pièces ?
    if ramassage_piece(i,j):
        compteur_pieces+=1
        print("Nombre de pièces récupérées",compteur_pieces)

    # Ramasser clefs ?
    if ramassage_clef(i,j):
        compteur_clefs=compteur_clefs+1
        print("Nombre de clefs récupérées",compteur_clefs)

    # Potion récupérée ?
    if potion_recupere(i,j):
        PV+=5
        print("PV : ",PV)

    # Ramasser arme ?
    if arme_recupere(i,j):
        perso=perso_arme

    # Ramasser bouton ?
    if bouton_recupere(i,j):
        compteur_bouton+=1
        mur_casse=herbe

    # Ennemi tué
    if ennemi_tue(i,j):
        compteur_ennemis+=1

    # bouton récupérée ?
    casse_mur(i,j)

    # Tous les objets récupérés ?
    if herbe_cache(i,j):
        compteur_herbe+=1

    # Entrée dans le temple
    if temple_recup(i,j):
        compteur_temple+=1

    if marche_eau(i,j):
        PV-=1
        print("PV : ",PV)

    # Perdu ?
    if PV<=0:
        perdu=True
        continuer=False

    # Gagné ?
    if compteur_pieces==3 and compteur_clefs==2 and compteur_temple:
        gagner=True
        continuer=False

    marche_eau(i,j)

    #Re-collage
    fenetre.blit(fond_niveau,(0,0))
    affiche_objets(liste_objets)#          <--
    fenetre.blit(perso,position_perso)#       |
    # --> affiche_objets(liste_objets)    ou ici

    # Rafraîchissement

    pygame.display.flip()

if perdu:
    fond_you_lose = pygame.image.load(image_you_lose).convert_alpha()
    fond_you_lose = pygame.transform.scale(fond_you_lose,(longueur_fenetre,largeur_fenetre))
    fenetre.blit(fond_you_lose,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)

# Victoire
if gagner:
    fond_you_win = pygame.image.load(image_you_win).convert_alpha()
    fond_you_win = pygame.transform.scale(fond_you_win,(longueur_fenetre,largeur_fenetre))
    fenetre.blit(fond_you_win,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)

# Fermeture fenêtre
pygame.quit()