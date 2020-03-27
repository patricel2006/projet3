"""
Jeu Mac Gyver Labyrinthe
Jeu dans lequel Mac Gyver doit récupérer 3 objets nécessaires pour endormir le garde et sortir du labyrinthe.
Script Python
Fichiers : mglabyrinthe.py, mgclasses.py, mgconstantes.py, design, + images
"""

import pygame
from pygame.locals import *

from mgclasses import *
from mgconstantes import *

pygame.init()

# Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
# Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
# Titre
pygame.display.set_caption(titre_fenetre)

# BOUCLE PRINCIPALE
continuer = 1
while continuer:
    # Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0, 0))

    # Rafraichissement
    pygame.display.flip()

    # On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    # BOUCLE D'ACCUEIL
    while continuer_accueil:

        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        # attente des entrées clavier utilisateur :
        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met les variables
            # de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                # Variable de choix de quitter ou de jouer :
                choix = 0

            elif event.type == KEYDOWN:
                # Lancement du jeu :
                if event.key == K_F1:
                    continuer_accueil = 0  # On quitte l'accueil
                    choix = 'design'  # On définit l'architecture du jeu dans un fichier

    # on vérifie que le joueur a bien fait le choix de commencer à jouer
    # pour ne pas charger s'il quitte
    if choix != 0:
        # Chargement du fond
        fond = pygame.image.load(image_fond).convert()
        fenetre.blit(fond, (0, 0))

        # Génération du design à partir d'un fichier design
        niveau = Niveau(choix)  # choix a pris la valeur du fichier 'design' ligne 61
        niveau.generer()
        niveau.afficher(fenetre)

        # Création du personnage de Mac Gyver :
        #mg = Perso("images/macgyver.png", niveau)
        mg = pygame.image.load(image_icone).convert_alpha()
        fenetre.blit(mg, (0, 0))

    # BOUCLE DE JEU
    while continuer_jeu:

        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met la variable qui continue le jeu
            # ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN:
                # Si l'utilisateur presse Echap ici, on revient seulement à l'accueil :
                if event.key == K_ESCAPE:
                    continuer_jeu = 0

                # Touches de déplacement de Donkey Kong
                elif event.key == K_RIGHT:
                    mg.deplacer('droite')
                elif event.key == K_LEFT:
                    mg.deplacer('gauche')
                elif event.key == K_UP:
                    mg.deplacer('haut')
                elif event.key == K_DOWN:
                    mg.deplacer('bas')

        # Affichages aux nouvelles positions
        #fenetre.blit(fond, (0, 0))
        #niveau.afficher(fenetre)
        # fenetre.blit(mg.direction, (mg.x, mg.y))  # mg.direction = l'image dans la bonne direction
        pygame.display.flip()

        # Victoire -> Retour à l'accueil
        #if niveau.structure[mg.case_y][mg.case_x] == 'a':
            #continuer_jeu = 0