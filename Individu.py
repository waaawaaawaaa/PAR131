"""Classe individu qui represente une possibilite de surface."""
import numpy as np
import random
from decimal import Decimal, getcontext

# Définir la précision globale (par exemple, 10 décimales)
getcontext().prec = 15

class Individu:
    """
    Classe qui represente un individu c'est-a-dire une surface.

    ...

    Attributes
    ----------
    hauteurs : np.array of floats
        Hauteurs de chaque asperite.
    rayons_courbure : np.array of floats
        Rayons de courbure de chaque asperite.

    Methods
    -------
    get_hauteur(i: int, j: int) -> float
        Obtient la hauteur d'une asperite.
    set_hauteur(i: int, j: int, valeur: float)
        Définit la hauteur d'une asperite.
    get_hauteurs() -> np.array of floats
        Obtient les hauteurs des asperites.

    """

    def __init__(self, individu1=None, individu2=None):
        """
        Initialise une instance de Individu.

        Parameters
        ----------
        Individu1 : Individu
            Individu père s'il s'agit d'un Individu enfant, sinon None.
        Individu2 : Individu
            Individu mère s'il s'agit d'un Individu enfant, sinon None.

        Returns
        -------
        None.

        """
        if individu1 is None:
            self.__hauteurs = self.__hauteurs_aleatoires()
        else:
            self.__hauteurs = self.__hauteurs_fusion(individu1, individu2)
        self.__rayons_courbure = np.array([[0.000526 for i in range(8)]
                                          for j in range(8)])

    def __hauteurs_aleatoires(self):
        """
        Cree aleatoirement les hauteurs de l'Individu.

        Returns
        -------
        hauteurs : np.array of floats
            Ensemble des hauteurs de l'Individu enfant.

        """
        hauteurs = np.array([[0 for i in range(8)] for j in range(8)])
        for i in range(8):
            for j in range(8):
                # On veut etre dans 0um et 120um avec une precision de 1um
                # Decimal permet d'eviter l'arrondi a 0
                hauteur = Decimal(random.randint(0, 120) / 10**6)
                hauteurs[i][j] = hauteur
        return hauteurs

    def __hauteurs_fusion(self, individu1, individu2):
        """
        Fusionne les hauteurs des Individus parents pour avoir celles enfants.

        Parameters
        ----------
        Individu1 : Individu
            Individu père.
        Individu2 : Individu
            Individu mère.

        Returns
        -------
        hauteurs : np.array of floats
            Ensemble des hauteurs de l'Individu enfant.

        """
        coupure = random.randint(1, 63)  # Valeur de changement du gene pris
        hauteurs = np.array([[0 for i in range(8)] for j in range(8)])
        for i in range(8):
            for j in range(8):
                if 8*i + j < coupure:  # Si on est avant la coupure
                    hauteurs[i][j] = individu1.get_hauteur(i, j)
                else:
                    hauteurs[i][j] = individu2.get_hauteur(i, j)
        return hauteurs

    def get_hauteur(self, i, j):
        """
        Obtient la hauteur d'une asperite.

        Parameters
        ----------
        i : int
            Premiere coordonnee de l'asperite.
        j : int
            Seconde coordonnee de l'asperite.

        Returns
        -------
        float
            Valeur de la hauteur de l'asperite.

        """
        return self.__hauteurs[i][j]

    def set_hauteur(self, i, j, valeur):
        """
        Définit la hauteur d'une asperite.

        Parameters
        ----------
        i : int
            Premiere coordonnee de l'asperite.
        j : int
            Seconde coordonnee de l'asperite.
        valeur : float
            Valeur de la hauteur de l'asperite.

        Returns
        -------
        None.

        """
        self.__hauteurs[i][j] = valeur

    def get_hauteurs(self):
        """
        Obtient les hauteurs des asperites.

        Returns
        -------
        np.array of floats
            Valeur des hauteurs des asperites.

        """
        return self.__hauteurs

    def get_rayons_courbure(self):
        """
        Obtient les rayons de courbure des asperites.

        Returns
        -------
        np.array of floats
            Valeur des rayons de courbure des asperites.

        """
        return self.__rayons_courbure


if __name__ == "__main__":
    individu = Individu()
