"""Module utilisant un algorithme génétique."""

import Algo_direct_v2
from Individu import Individu
import random
import affichage


def creer_individu():
    """
    Cree un individu de la premiere generation.

    Returns
    -------
    individu : Individu
        Individu creer aleatoirement.

    """
    individu = Individu()
    return individu


def creer_population(N):
    """
    Cree la population entiere.

    Parameters
    ----------
    N : integer
        Nombre d'individus dans la population.

    Returns
    -------
    population : list of Individus
        Liste de l'ensemble des N individus.

    """
    population = []
    for i in range(N):
        population.append(creer_individu())
    return population


def score(individu, points):
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
    for point in points:
        aire = Algo_direct_v2.get_aire_totale(individu.get_rayons_courbure(),
                                              individu.get_hauteurs(),
                                              point[0])
        score = score + (point[1] - aire)**2
    return score


def selection(population, points):
    """
    Selectionne les meilleurs individus de la population.

    Parameters
    ----------
    population : list of Individus
        Population entiere d'une generation.
    points : list of couple of floats
        Points (force, aire_totale) du cahier des charges

    Returns
    -------
    population_selectionnee : list of Individus
        Population avec les individus selectionnes

    """
    population_triee = sorted(population,
                              key=lambda individu: score(individu, points))
    population_selectionnee = population_triee[:round(len(population)/2)]
    return population_selectionnee


def enjambement(individu1, individu2):
    """
    Realise l'enjambement entre deux individus.

    Parameters
    ----------
    individu1 : Individu
        Premiere individu.
    individu2 : Individu
        Deuxieme individu.

    Returns
    -------
    individu_enfant : Individu
        Individu issu de l'enjambement.

    """
    return Individu(individu1, individu2)


def nouvelle_generation(population, points):
    """
    Cree la nouvelle generation.

    Parameters
    ----------
    population : list of Individus
        Population de l'ancienne generation.
    points : list of couple of floats
        Points (force, aire_totale) du cahier des charges

    Returns
    -------
    nouvelle_population : list of Individus
        Population de la nouvelle generation.

    """
    nouvelle_population = selection(population, points)
    N = len(nouvelle_population)
    for i in range(0, N, 2):
        nouvelle_population.append(Individu(nouvelle_population[i],
                                            nouvelle_population[i+1]))
        nouvelle_population.append(Individu(nouvelle_population[i+1],
                                            nouvelle_population[i]))
    return nouvelle_population


def mutation(population):
    """
    Realise les potentielles mutations.

    Parameters
    ----------
    population : list of Individus
        Population initiale.

    Returns
    -------
    None

    """
    probabilite = 0.001  # Probabilite de mutation d'un gene
    for individu in population:
        for i in range(len(individu.get_hauteurs())):
            for j in range(len(individu.get_hauteurs()[i])):
                if random.random() < probabilite:  # S'il y a mutation
                    hauteur = random.randint(0, 120)  # En um
                    individu.set_hauteur(i, j, hauteur)


def genetique(points, limite=None):
    """
    Realise l'algorithme génétique d'optimisation.

    Parameters
    ----------
    points : list of pairs of floats
        Liste des points (force, aire de contact) du cahier des charges.
    limite : float
        Valeur des moindres carrés pour l'acceptabilité.

    Returns
    -------
    None.

    """
    N = 50  # Taille de la population
    population = creer_population(N)
    for i in range(100):  # On fait 100 generations
        print('fdjkl')
        population = nouvelle_generation(population, points)
        print('rgfidskodf')
        mutation(population)
        print("icicicici")
        meilleur_individu = selection(population, points)[0]
        print(score(meilleur_individu, points))
        aires, forces = Algo_direct_v2.loi_totale(meilleur_individu.get_rayons_courbure(),
                                                  meilleur_individu.get_hauteurs())
        affichage.superposer_lois([(aires,forces)], points=points)
    affichage.loi(aires, forces)
    affichage.hauteur(meilleur_individu.get_hauteurs())


if __name__ == "__main__":
    print('djk')
    genetique([(0.0215*10**14, 1.5), (0.0243*10**14, 5.1)])
