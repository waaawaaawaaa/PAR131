"""Module qui permet le calcul des aires de contact et des forces."""

import numpy as np
import affichage
import random


def loi_indentation(rayons_courbure, hauteurs, delta):
    """
    Realise le calcul des aires de contact et de la force totale.

    Parameters
    ----------
    rayons_courbure : np.array of floats
        Liste avec les rayons de courbures des spheres.
    hauteurs : np.array of floats
        Liste avec les hauteurs des spheres.
    delta : float
        Indentation totale.

    Returns
    -------
    aires_contact : np.array of floats
        Liste avec les aires de contact de chaque sphere.
    force_tot : float
        Force totale exercee.

    """
    E_etoile = 1.36 * 10 ** 6  # Valeur de la slide 24 du diapo de A. Aymard
    hauteur_max = np.max(hauteurs)  # Donne la hauteur la plus elevee
    # Calcul de la force i selon la slide 27, en 10**12
    deltas = np.maximum(delta + hauteurs - hauteur_max, 0)
    forces = (4/3 * E_etoile
              * np.sqrt(rayons_courbure * np.pi)
              * deltas
              ** (3/2))
    force_tot = np.sum(forces)
    aires_contact = np.pi * rayons_courbure * deltas
    return aires_contact, force_tot


def loi_totale(rayons_courbure, hauteurs):
    """
    Realise le calcule des points pour la courbe aire en fonction de la force.

    Parameters
    ----------
    rayons_courbure : np.array of floats
        Liste avec les rayons de courbure des spheres.
    hauteurs : np.array of floats
        Liste avec les hauteurs des spheres.

    Returns
    -------
    aires_totales : list numpy of floats
        Valeurs des aires de contact totale en fonction de la force.
    forces_totales : list numpy of float
        Valeurs des forces.

    """
    N = 10000  # Nombre de points
    hauteur_max = np.max(hauteurs)  # Donne la hauteur la plus elevee
    E_etoile = 1.36 * 10 ** 6  # Valeur de la slide 24 du diapo de A. Aymard
    deltas = np.maximum(np.ones((len(hauteurs), 1))
                        * np.arange(0, N)
                        + hauteurs.reshape(len(hauteurs), 1) * np.ones((1, N))
                        - hauteur_max,
                        0)
    aires_contact = (np.pi
                     * np.multiply(rayons_courbure.reshape(len(hauteurs), 1),
                                   deltas))
    forces = (4/3 * E_etoile * np.sqrt(np.pi)
              * np.multiply(
              np.sqrt(rayons_courbure.reshape(len(hauteurs), 1)),
              deltas**(3/2)))
    aires_totales = np.sum(aires_contact, 0)  # Aire de contacte totale
    forces_totales = np.sum(forces, 0)
    return aires_totales, forces_totales


def get_force_aire(rayons_courbure, hauteurs, point):
    """Retrouve les points necessaires aux scores.

    A partir d'un point, retrouve la force correspondant a l'aire de ce
    point et l'aire correspondant a la force de ce point.

    Parameters
    ----------
    rayons_courbure : np.array of floats
        Liste avec les rayons de courbure des spheres.
    hauteurs : np.array of floats
        Liste avec les hauteurs des spheres.
    point : couple of float
        Point que l'on souhaite atteindre (force, aire)

    Returns
    -------
    force : float
        Force correspondant a l'aire du point
    aire : float
        Aire totale correspondant a la force du point
    """
    aires, forces = loi_totale(rayons_courbure, hauteurs)
    i = min(range(len(forces)), key=lambda i: abs(forces[i] - point[0]))
    j = min(range(len(aires)), key=lambda j: abs(aires[j] - point[1]))
    return aires[i], forces[j]


if __name__ == "__main__":
    # valeur de rayon de courbure issue des transparents de A.Aymard slide 39
    # valeurs en um
    rayons_courbure = np.array([526 for i in range(64)])
    hauteurs = np.array([random.randint(0, 120) for i in range(64)])
    aires_totales, forces_totales = loi_totale(rayons_courbure, hauteurs)
    affichage.loi(aires_totales, forces_totales)
    affichage.hauteur(hauteurs)
