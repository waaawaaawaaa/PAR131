# -*- coding: utf-8 -*-


"""Module utilisant un algorithme génétique."""

import random
import time
import multiprocessing
import csv
import psutil
import numpy as np
from functools import partial
from individu import Individu
import affichage
import algo_direct

nombre_coeurs = psutil.cpu_count(logical=False)


def creer_individu(points, _):
    """
    Cree un individu de la premiere generation.

    Parameters
    ----------
    points : list of couple of floats
        Points (force, aire_totale) du cahier des charges.
    _ : integer
        Numero de l'element dans la liste, sert pour l'utilisation de pool.map.

    Returns
    -------
    individu : Individu
        Individu creer aleatoirement.

    """
    individu = Individu()
    individu.set_score(points)
    return individu


def creer_population(taille_population, points):
    """
    Cree la population entiere pour la premiere generation.

    Parameters
    ----------
    taille_population : integer
        Nombre d'individus dans la population.
    points : list of couple of floats
        Points (force, aire_totale) du cahier des charges.

    Returns
    -------
    population : list of Individus
        Liste de l'ensemble des N individus.

    """
    # On cree une version de la fonction creer_individu sans arguments d'entree
    creer_individu_partiel = partial(creer_individu, points)

    with multiprocessing.Pool() as pool:
        # Utilisation de pool.map pour créer tous les individus en parallèle
        population = pool.map(creer_individu_partiel, range(taille_population))
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
        Population avec les individus selectionnes.

    """
    population_triee = sorted(population,
                              key=lambda individu: individu.get_score())
    population_selectionnee = population_triee[:round(len(population)/2)]
    return population_selectionnee


def individu_enfant(nouvelle_population, points, i):
    """
    Cree un individu enfant.

    Parameters
    ----------
    nouvelle_population : list of Individus
        Population des parents de la generation precedente.
    points : list of couple of floats
        Points (force, aire_totale) du cahier des charges.
    i : integer
        Numero de l'individu enfant.

    Returns
    -------
    individu : Individu
        Individu enfant.

    """
    individu = mutation(Individu(nouvelle_population[i],
                                 nouvelle_population[i+1]),
                        points)
    return individu


def nouvelle_generation(population, points):
    """
    Cree la nouvelle generation.

    Parameters
    ----------
    population : list of Individus
        Population de l'ancienne generation.
    points : list of couple of floats
        Points (force, aire_totale) du cahier des charges.

    Returns
    -------
    nouvelle_population : list of Individus
        Population de la nouvelle generation.

    """
    nouvelle_population = selection(population)
    taille_population = len(nouvelle_population)
    # Fonction individu_enfant avec que l'indice de l'individu en entree
    individu_enfant_partiel = partial(individu_enfant, nouvelle_population,
                                      points)

    with multiprocessing.Pool() as pool:
        # Utilisation de pool.map pour créer tous les individus en parallèle
        population_enfant = pool.map(individu_enfant_partiel,
                                     range(taille_population - 1))

    nouvelle_population = nouvelle_population + population_enfant
    return nouvelle_population


def mutation(individu, points):
    """
    Realise les potentielles mutations sur un individu.

    Parameters
    ----------
    individu : Individu
        Individu pouvant subir une mutation.
    points : list of couple of floats
        Points (force, aire_totale) du cahier des charges.

    Returns
    -------
    individu : Individu
        Individu apres la mutation.

    """
    probabilite = 0.4  # Probabilite de mutation d'un gene
    individu.mutation(probabilite)
    individu.set_score(points)
    return individu


def genetique(points, n=None):
    """
    Realise l'algorithme génétique d'optimisation.

    Parameters
    ----------
    points : list of pairs of floats
        Liste des points (force, aire de contact) du cahier des charges.
    n : integer
        Numero du test de l'algorithme.

    Returns
    -------
    np.array of floats
        Valeur des hauteurs des asperites.

    """
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
    i = 0  # Numero de la generation
    # while i <= 20 or not liste_score[-20] == liste_score[-1]:
    # while len(liste_score) == 0 or liste_score[-1] > 10**(-8):
    for i in range(500):
        population = nouvelle_generation(population, points)
        meilleur_individu = selection(population)[0]
        # print("Génération : ", i)
        # print(meilleur_individu.get_score())
        liste_score.append(meilleur_individu.get_score())
        # if i % 100 == 0:
            # forces, aires = algo_direct.loi_totale(
                           # meilleur_individu.get_rayons_courbure(),
                           # meilleur_individu.get_hauteurs())
            # affichage.hauteur(meilleur_individu.get_hauteurs())
            # affichage.superposer_loi_points(forces, aires, points, i,
            #   liste_score[i])
            # affichage.score(liste_score)
        # i += 1
    # print(meilleur_individu.set_score(points, False))  # Score sans les poids
    # print(meilleur_individu.get_score())
    # print(meilleur_individu.get_rayons_courbure())
    forces, aires = algo_direct.loi_totale(
                    meilleur_individu.get_rayons_courbure(),
                    meilleur_individu.get_hauteurs())
    affichage.score(liste_score, n)
    affichage.superposer_loi_points(forces, aires, points, i, liste_score[i],
                                    n)
    affichage.hauteur(meilleur_individu.get_hauteurs(), n)
    return meilleur_individu.get_hauteurs()


if __name__ == "__main__":
    # debut = time.time()
    liste = []
    for n in range(10):
        hauteurs = genetique([(18384800256 * (90*i+1),
                               18384800256 * (90*i+1) * 3.1069013782046355e-06)
                              for i in range(10)],
                             n)
        moyenne = np.mean(hauteurs)
        moments = {'numéro': n,
                   'moyenne': np.mean(hauteurs),
                   'variance': np.var(hauteurs),
                   'asymétrie': np.mean((hauteurs - moyenne)**3),
                   'kurtosis': np.mean((hauteurs - moyenne)**4)}
        liste.append(moments)

    with open('save.csv', 'w', newline='') as csvfile:
        fieldnames = list(moments.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for moments in liste:
            writer.writerow(moments)

    # print(time.time() - debut)
