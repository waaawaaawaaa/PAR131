"""Module utilisant un algorithme génétique."""

import Algo_direct_v2


def creer_individu():
    """
    Cree un individu de la premiere generation.

    Returns
    -------
    individu : Individu
        Individu creer aleatoirement.

    """
    pass


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


def score(individu):
    """
    Definit le score de l'individu.

    Parameters
    ----------
    individu : Individu
        Individu dont on va calculer le score.

    Returns
    -------
    score : float
        Score obtenu par la methode des moindres carres

    """
    pass


def selection(population):
    """
    Selectionne les meilleurs individus de la population.

    Parameters
    ----------
    population : list of Individus
        Population entiere d'une generation.

    Returns
    -------
    population_selectionnee : list of Individus
        Population avec les individus selectionnes/

    """
    pass


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
    pass


def nouvelle_generation(population):
    """
    Cree la nouvelle generation.

    Parameters
    ----------
    population : list of Individus
        Population de l'ancienne generation.

    Returns
    -------
    nouvelle_population : list of Individus
        Population de la nouvelle generation.

    """
    pass


def mutation(population):
    """
    Realise les potentielles mutations.

    Parameters
    ----------
    population : list of Individus
        Population initiale.

    Returns
    -------
    population_mutee : list of Individus
        Population avec des potentielles mutations.

    """
    pass


def genetique(points, limite):
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
    N = 100  # Taille de la population
