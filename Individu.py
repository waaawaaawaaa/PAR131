"""Classe individu qui represente une possibilite de surface."""
import numpy as np
import random

nombre_asperites = 64


class Individu:
    """
    Classe qui represente un individu c'est-a-dire une surface.

    ...

    Attributes
    ----------
    hauteurs : np.array of floats
        Hauteurs de chaque asperite.
    rayons : np.array of floats
        Rayons de courbure de chaque asperite.

    Methods
    -------
    get_hauteur(i: int, j: int) -> float
        Obtient la hauteur d'une asperite.
    set_hauteur(i: int, j: int, valeur: float)
        Définit la hauteur d'une asperite.
    get_hauteurs() -> np.array of floats
        Obtient les hauteurs des asperites.
    get_rayons_courbure -> np.array of floats
        Obtient les rayons de courbure des asperites.

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
            self.__rayons = self.__rayons_aleatoires()
        else:
            self.__hauteurs = self.__hauteurs_fusion(individu1, individu2)
            self.__rayons = self.__rayons_fusion(individu1, individu2)

    def __hauteurs_aleatoires(self):
        """
        Cree aleatoirement les hauteurs de l'Individu.

        Returns
        -------
        hauteurs : np.array of floats
            Ensemble des hauteurs de l'Individu enfant.

        """
        # On veut etre dans 0um et 120um avec une precision de 1um
        # Hauteurs en um
        hauteurs = np.array([random.randint(0, 120) for i
                             in range(nombre_asperites)])
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
        # Probabilite de prendre les genes du pere.
        seuil = random.random()
        hauteurs = np.array([0 for i in range(nombre_asperites)])
        for i in range(nombre_asperites):
            test = random.random()
            if test < seuil:  # Si on est avant la coupure
                hauteurs[i] = individu1.get_hauteur(i)
            else:
                hauteurs[i] = individu2.get_hauteur(i)
        return hauteurs

    def get_hauteur(self, i):
        """
        Obtient la hauteur d'une asperite.

        Parameters
        ----------
        i : int
            Coordonnee de l'asperite.

        Returns
        -------
        float
            Valeur de la hauteur de l'asperite.

        """
        return self.__hauteurs[i]

    def set_hauteur(self, i, valeur):
        """
        Définit la hauteur d'une asperite.

        Parameters
        ----------
        i : int
            Coordonnee de l'asperite.
        valeur : float
            Valeur de la hauteur de l'asperite.

        Returns
        -------
        None.

        """
        self.__hauteurs[i] = valeur

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
        return self.__rayons

    def __rayons_aleatoires(self):
        """
        Cree aleatoirement les rayons de l'Individu.

        Returns
        -------
        rayons : np.array of floats
            Ensemble des rayons de l'Individu enfant.

        """
        # On veut etre dans 100um et 530um avec une precision de 10um
        # rayons en um
        rayons = np.array([10 * random.randint(10, 53) for i
                           in range(nombre_asperites)])
        return rayons

    def __rayons_fusion(self, individu1, individu2):
        """
        Fusionne les rayons des Individus parents pour avoir celles enfants.

        Parameters
        ----------
        Individu1 : Individu
            Individu père.
        Individu2 : Individu
            Individu mère.

        Returns
        -------
        rayons : np.array of floats
            Ensemble des rayons de l'Individu enfant.

        """
        # Probabilite de prendre les genes du pere.
        seuil = random.random()
        rayons = np.array([0 for i in range(nombre_asperites)])
        for i in range(nombre_asperites):
            test = random.random()
            if test < seuil:  # Si on est avant la coupure
                rayons[i] = individu1.get_rayon(i)
            else:
                rayons[i] = individu2.get_rayon(i)
        return rayons

    def get_rayon(self, i):
        """
        Obtient le rayon d'une asperite.

        Parameters
        ----------
        i : int
            Coordonnee de l'asperite.

        Returns
        -------
        float
            Valeur de la rayon de l'asperite.

        """
        return self.__rayons[i]

    def set_rayon(self, i, valeur):
        """
        Définit le rayon d'une asperite.

        Parameters
        ----------
        i : int
            Coordonnee de l'asperite.
        valeur : float
            Valeur de la rayon de l'asperite.

        Returns
        -------
        None.

        """
        self.__rayons[i] = valeur


if __name__ == "__main__":
    individu = Individu()
