"""Module utilisant un algorithme génétique."""

import random
import time
from Individu import Individu, changement_rayons
import affichage
import algo_direct


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


def creer_population(taille_population, points):
    """
    Cree la population entiere pour la premiere generation.

    Parameters
    ----------
    taille_population : integer
        Nombre d'individus dans la population.
    points : list of couple of floats
        Points (force, aire_totale) du cahier des charges

    Returns
    -------
    population : list of Individus
        Liste de l'ensemble des N individus.

    """
    population = []
    for i in range(taille_population):
        individu = creer_individu()
        individu.set_score(points)
        population.append(individu)
    return population


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
        Population avec les individus selectionnes

    """
    population_triee = sorted(population,
                              key=lambda individu: individu.get_score())
    population_selectionnee = population_triee[:round(len(population)/2)]
    return population_selectionnee


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
    nouvelle_population = selection(population)
    taille_population = len(nouvelle_population)
    for i in range(0, taille_population-1, 2):
        individu1 = mutation(Individu(nouvelle_population[i],
                                      nouvelle_population[i+1]))
        individu2 = mutation(Individu(nouvelle_population[i+1],
                                      nouvelle_population[i]))
        individu1.set_score(points)
        individu2.set_score(points)
        nouvelle_population.append(individu1)
        nouvelle_population.append(individu2)
    return nouvelle_population


def mutation(individu):
    """
    Realise les potentielles mutations sur un individu.

    Parameters
    ----------
    individu : Individu
        Individu pouvant subir une mutation.

    Returns
    -------
    individu : Individu
        Individu apres la mutation.

    """
    probabilite = 0.1  # Probabilite de mutation d'un gene
    for i in range(len(individu.get_hauteurs())):
        if random.random() < probabilite:  # S'il y a mutation sur la hauteur
            hauteur = random.randint(0, 120)  # En um
            individu.set_hauteur(i, hauteur)
    if changement_rayons:
        for i in range(len(individu.get_rayons_courbure())):
            if random.random() < probabilite:  # S'il y a mutation sur le rayon
                rayon = 10 * random.randint(10, 53)  # En um
                individu.set_rayon(i, rayon)
    return individu


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
    liste_courbes = []
    liste_score = []

    taille_population = 50  # Taille de la population
    population = creer_population(taille_population, points)
    # for individu in population:

    #     forces, aires = algo_direct.loi_totale(
    #                     individu.get_rayons_courbure(),
    #                     individu.get_hauteurs())
    #     liste_courbes.append((forces, aires))
    #     affichage.superposer_lois(liste_courbes, points=points)
    # affichage.loi(forces, aires)
    # affichage.hauteur(individu.get_hauteurs())

    # return

    for i in range(1000):  # On fait 100 generations
        population = nouvelle_generation(population, points)
        meilleur_individu = selection(population)[0]
        print("Génération : ", i)
        print(meilleur_individu.get_score())
        liste_score.append(meilleur_individu.get_score())
        forces, aires = algo_direct.loi_totale(
                        meilleur_individu.get_rayons_courbure(),
                        meilleur_individu.get_hauteurs())
        liste_courbes.append((forces, aires))
        affichage.superposer_loi_points(forces, aires, points, i,
                                        liste_score[i])
        affichage.score(liste_score)
    meilleur_individu.set_score(points, False)  # Score sans les poids
    print(meilleur_individu.get_score())
    print(meilleur_individu.get_rayons_courbure())
    affichage.score(liste_score)
    affichage.loi(forces, aires)
    affichage.hauteur(meilleur_individu.get_hauteurs())


if __name__ == "__main__":
    debut = time.time()
    genetique([(558208229327, 1956593), (558208229327*2, 1956593*2)])
    print(time.time() - debut)
