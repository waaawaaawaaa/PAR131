"""Classe individu qui represente une possibilite de surface."""
import random
import numpy as np
import algo_direct


class Individu:
    """
    Classe qui represente un individu c'est-a-dire une surface.

    ...

    Attributes
    ----------
    nombre_asperites : integer
        Nombre d'asperites de l'ensemble des individus.
    changement_rayons : boolean
        Presence ou non des rayons comme genes pour nos individus.
    hauteurs : np.array of floats
        Hauteurs de chaque asperite.
    rayons : np.array of floats
        Rayons de courbure de chaque asperite.
    score : float
        Score de notre individu.

    Public methods
    -------
    get_hauteur(i: int) -> float
        Obtient la hauteur d'une asperite.
    set_hauteur(i: int, valeur: float)
        Definit la hauteur d'une asperite.
    get_hauteurs() -> np.array of floats
        Obtient les hauteurs des asperites.
    get_rayons_courbure -> np.array of floats
        Obtient les rayons de courbure des asperites.
    get_rayon(i: int) -> float
        Obtient le rayon d'une asperite.
    set_rayon(i: int, valeur: float)
        Definit le rayon d'une asperite.
    set_score(points: list of couple of floats, poids: boolean)
        Definit le score de l'individu.
    get_score() -> float
        Obtient le score d'un individu.
    mutation(probabilite: float)
        Realise la mutation de l'individu.

    Private methods
    -------
    __hauteurs_aleatoires() -> np.array of floats
        Cree aleatoirement les hauteurs de l'Individu.
    __hauteurs_fusion(individu1: Individu, individu2: Individu)
                      -> np of array of floats
        Fusionne les hauteurs des Individus parents pour avoir celles enfants.
    __rayons_aleatoires() -> np.array of floats
        Cree aleatoirement les rayons de l'Individu.
    __rayons_fusion(individu1: Individu, individu2: Individu)
                      -> np of array of floats
        Fusionne les rayons des Individus parents pour avoir celles enfants.
    """

    nombre_asperites = 1000
    changement_rayons = False

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
        if self.changement_rayons:
            if individu1 is None:
                self.__hauteurs = self.__hauteurs_aleatoires()
                self.__rayons = self.__rayons_aleatoires()
            else:
                self.__hauteurs = self.__hauteurs_fusion(individu1, individu2)
                self.__rayons = self.__rayons_fusion(individu1, individu2)
        else:
            if individu1 is None:
                self.__hauteurs = self.__hauteurs_aleatoires()
            else:
                self.__hauteurs = self.__hauteurs_fusion(individu1, individu2)
            self.__rayons = np.array([526 for i in range(
                                      self.nombre_asperites)])
        self.__score = 0

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
                             in range(self.nombre_asperites)])
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
        hauteurs = np.array([0 for i in range(self.nombre_asperites)])
        for i in range(self.nombre_asperites):
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
                           in range(self.nombre_asperites)])
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
        rayons = np.array([0 for i in range(self.nombre_asperites)])
        for i in range(self.nombre_asperites):
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

    def set_score(self, points, poids=True):
        """
        Definit le score de l'individu.

        Parameters
        ----------
        individu : Individu
            Individu dont on va calculer le score.
        points : list of couple of floats
            Points (force, aire_totale) du cahier des charges

        Returns
        -------
        score : float
            Score obtenu par la methode des moindres carres

        """
        score = 0
        aire_0 = points[-1][1]  # Aire pour normalisee
        force_0 = points[-1][0]  # Force pour normalisee
        forces, aires = algo_direct.loi_totale(self.get_rayons_courbure(),
                                               self.get_hauteurs())
        for i, point in enumerate(points):
            force, aire = algo_direct.get_force_aire(forces, aires, point)
            if i == 0 and poids:
                score = (1 * (((point[1] - aire)/aire_0)**2
                         + ((point[0] - force)/force_0)**2))
            else:
                score = (score + ((point[1] - aire)/aire_0)**2
                         + ((point[0] - force)/force_0)**2)
        if poids:
            self.__score = score/len(points)
        else:
            self.__score = score/len(points)

    def get_score(self):
        """
        Obtient le score d'un individu.

        Returns
        -------
        float
            Score de l'individu.

        """
        return self.__score

    def mutation(self, probabilite):
        """
        Realise la mutation de l'individu.

        Parameters
        ----------
        probabilite : float
            Probabilite pour un gene de muter.

        Returns
        -------
        None.

        """
        for i in range(len(self.__hauteurs)):
            if random.random() < probabilite:  # Si mutation sur la hauteur
                delta = random.randint(-5, 5)  # En um
                if self.__hauteurs[i] + delta < 0:
                    hauteur = 0
                elif self.__hauteurs[i] + delta > 120:
                    hauteur = 120
                else:
                    hauteur =self.__hauteurs[i] + delta
                self.set_hauteur(i, hauteur)
        if self.changement_rayons:
            for i in range(len(self.__rayons)):
                if random.random() < probabilite:  # Si a mutation sur le rayon
                    rayon = 10 * random.randint(10, 53)  # En um
                    self.set_rayon(i, rayon)


if __name__ == "__main__":
    individu = Individu()
