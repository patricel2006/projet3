"""Classes du jeu de Labyrinthe Mac Gyver"""

import pygame
from pygame.locals import *
from mgconstantes import *


class Niveau:
    """Classe permettant de créer un niveau"""

    # méthode qui implémente la capacité de charger un fichier :
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self):
        """Méthode permettant de générer le labyrinthe à partir du fichier contenant son design.
        La grille est encodée grace à deux boucles for."""
        # ouverture du fichier contenant le design :
        with open(self.fichier, "r") as fichier:
            # initialisation de ma grille sous forme de liste vide :
            structure_niveau = []
            # parcourt des lignes du fichier :
            for ligne in fichier:
                ligne_niveau = []
                # parcourt des sprites (lettres) contenues dans le fichier :
                for sprite in ligne:
                    # les "\n" de fin de ligne sont ignorés :
                    if sprite != '\n':
                        # On ajoute une case à la ligne :
                        ligne_niveau.append(sprite)
                # ajout de la ligne à la liste des lignes
                structure_niveau.append(ligne_niveau)
            # sauvegarde de la structure
            self.structure = structure_niveau

    def afficher(self, fenetre):
        """Méthode permettant d'afficher le labyrinthe en fonction
        de la grille renvoyée par generer()"""
        # Chargement des images :
        mg = pygame.image.load("images/macgyver.png").convert_alpha()
        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()

        # On parcourt toute la grille : lignes + colonnes :
        # initialisation du numéro de ligne à zéro :
        num_ligne = 0
        # boucle qui parcourt toutes les lignes de la grille :
        for ligne in self.structure:
            # On initialise le numéro de case à zéro :
            num_case = 0
            # boucle qui parcourt toutes les cases de la ligne :
            for sprite in ligne:
                # On calcule la position réelle en pixels en multipliant par la taille de chaque case (30 pixels)
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':  # m = Mur
                    # je colle l'image du mur sur la case correspondante :
                    fenetre.blit(mur, (x, y))
                elif sprite == 'd':  # d = Départ
                    # je colle l'image du départ sur la case qui convient :
                    fenetre.blit(depart, (x, y))
                elif sprite == 'a':  # a = Arrivée
                    fenetre.blit(arrivee, (x, y))
                num_case += 1
            num_ligne += 1


class Perso:
    """Classe permettant de créer le personnage de Mac Gyver"""

    def __init__(self, niveau, direction):

        # chargement de l'image de MG :
        self.mg = pygame.image.load("images/macgyver.png").convert_alpha()

        # Position du personnage en cases et en pixels :
        #self.case_x = 0
        #self.case_y = 0
        self.x_mg = 0
        self.y_mg = 0
        # Direction par défaut
        self.direction = direction
        # design du labyrinthe :
        self.niveau = niveau

    def deplacer(self, direction):
        """Methode permettant de déplacer MG"""

        self.direction = direction

        # affichage de la direction choisie :
        print(direction)

        # initialisation des coordonnées de MG :
        global x_mg
        global y_mg

        # Déplacement vers la droite :
        if self.direction == 'droite':
            x_mg = x_mg + 35

        # Déplacement vers la gauche
        if self.direction == 'gauche':
            x_mg = x_mg - 35

        # Déplacement vers le haut
        if self.direction == 'haut':
            y_mg = y_mg - 35

        # Déplacement vers le bas
        if self.direction == 'bas':
            y_mg = y_mg + 35

        print(str(x_mg))
        print(str(y_mg))
