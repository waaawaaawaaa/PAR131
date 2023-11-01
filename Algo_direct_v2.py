"""Module qui permet le calcul des aires de contact et des forces."""

import numpy as np
import affichage
import random
from numpy.random import exponential
from decimal import Decimal, getcontext

# Définir la précision globale (par exemple, 10 décimales)
getcontext().prec = 15


def loi_indentation(rayons_courbures, hauteurs, delta):
    """
    Realise le calcul des aires de contact et de la force totale.

    Parameters
    ----------
    rayons_courbures : np.array of floats
        Matrice avec les rayons de courbures des sphères.
    hauteurs : np.array of floats
        Matrice avec les hauteurs des sphères.
    delta : float
        Indentation totale.

    Returns
    -------
    aires_contact : np.array of floats
        Matrice avec les aires de contact de chaque sphère.
    force_tot : float
        Force totale exercee.

    """
    E_etoile = 1.36 * 10 ** 6  # Valeur de la slide 24 du diapo de A. Aymard
    hauteur_max = np.max(hauteurs)  # Donne la hauteur la plus elevee
    force_tot = Decimal(0)  # Donne la force totale
    aires_contact = np.zeros((len(rayons_courbures), len(rayons_courbures[0])))
    for i in range(len(rayons_courbures)):
        for j in range(len(rayons_courbures[0])):
            # On cherche l'identation i, vaut 0 si pas d'indentation
            delta_i = max(delta + hauteurs[i][j] - hauteur_max, 0)
            # Calcul de la force i selon la slide 27
            force_i = Decimal((4/3 * E_etoile
                               * np.sqrt(rayons_courbures[i][j] * np.pi)
                               * delta_i ** (3/2)))
            force_tot = force_tot + force_i
            aire_i = Decimal(np.pi * rayons_courbures[i][j] * delta_i)
            aires_contact[i][j] = aire_i
    return aires_contact, force_tot


def loi_totale(rayons_courbure, hauteurs):
    """
    Realise le calcule des points pour la courbe aire en fonction de la force.

    Parameters
    ----------
    rayons_courbure : np.array of floats
        Matrice avec les rayons de courbure des sphères.
    hauteurs : np.array of floats
        Matrice avec les hauteurs des sphères..

    Returns
    -------
    aires_totales : list of floats
        Valeurs des aires de contact totale en fonction de la force.
    forces_totales : list of float
        Valeurs des forces.

    """
    N = 10000  # Nombre de points
    aires_totales = []  # Liste des aires
    forces_totales = []  # Liste des forces
    hauteur_max = np.max(hauteurs)  # Donne la hauteur la plus elevee
    hauteur_moitie = (3*hauteur_max) / 4
    for i in range(N):
        delta = i * hauteur_max / N  # Valeur de l'indentation
        # On récupère les aires de chaque sphère et la force
        aires_contact, force = loi_indentation(rayons_courbure, hauteurs,
                                               delta)
        print(force)
        aire_totale = np.sum(aires_contact)  # Aire de contacte totale
        aires_totales.append(aire_totale)
        forces_totales.append(force)

        # if delta == hauteur_moitie:
        #     affichage.spheres(aires_contact)
    return aires_totales, forces_totales


def get_aire_totale(rayons_courbure, hauteurs, force):
    aires_totales, forces_totales = loi_totale(rayons_courbure, hauteurs)
    for i in range(len(forces_totales)):
        if round(forces_totales[i], 4) == force:  # Si on a la bonne force
            aire = aires_totales[i]
            return aire


if __name__ == "__main__":
    # valeur de rayon de courbure issue des transparents de A.Aymard slide 39
    rayons_courbures = np.array([[0.000526 for i in range(5)]
                                 for j in range(5)])
    hauteurs = np.array([[random.randint(0, 120) / 10**6 for i in range(8)] for j in range(8)])

    aires_totales, forces_totales = loi_totale(rayons_courbures, hauteurs)
    affichage.loi(aires_totales, forces_totales)
    affichage.hauteur(hauteurs)
