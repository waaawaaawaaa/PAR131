# -*- coding: utf-8 -*-


"""Module qui permet les differents affichages."""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.cm import ScalarMappable
import matplotlib.colors as mcolors
import numpy as np
import random


def spheres(aires):
    """
    Cree le graphique representant les spheres.

    Parameters
    ----------
    aires : np.array of floats
        Liste des aires des spheres, cela doit etre un carre.

    Returns
    -------
    None.

    """
    matrice_aires = [[aires[i+j] for i in range(np.sqrt(len(aires)))]
                     for j in range(np.sqrt(len(aires)))]
    fig, ax = plt.subplots()  # Cree le graphique

    cmap = plt.get_cmap('viridis')  # Choix du jeu de couleurs
    norm = mcolors.Normalize(vmin=np.min(matrice_aires),
                             vmax=np.max(matrice_aires))
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Permet l'utilisation d'une colorbar

    matrice_rayons = np.sqrt(matrice_aires/np.pi)

    espacement = 3 * np.max(matrice_rayons)  # Espace entre deux centres

    for i in range(len(matrice_aires)):  # Creation des cercles
        for j in range(len(matrice_aires[0])):
            color = cmap(norm(matrice_aires[i][j]))  # Couleur du cercle i, j
            circle = Circle((i * espacement, j * espacement),
                            radius=matrice_rayons[i][j],
                            fill=True, color=color)  # Cree le cercle i, j
            ax.add_patch(circle)  # Ajout du cercle

    cbar = plt.colorbar(sm, ax=ax)  # Ajoute la colorbar
    cbar.set_label('A\u1D3F (m²)')  # Titre de la colorbar

    # Limites des axes vallent les positions extremes decalees du rayon max
    ax.set_xlim(- espacement/2,
                (len(matrice_rayons) - 1) * espacement + espacement / 2)
    ax.set_ylim(- max(matrice_rayons[0]),
                (len(matrice_rayons[0]) - 1) * espacement + espacement / 2)

    # Affichez le graphique
    plt.axis('scaled')  # Permet un repere norme
    plt.xlabel('x')  # Nom de l'axe x
    plt.ylabel('y')  # Nom de l'axe y
    plt.savefig("images/aire.png")  # Permet de sauvegarder le fichier
    plt.close()  # Affiche le graphique


def loi(forces, aires):
    """
    Cree le graphique affichant l'aire de contact en fonction de la force.

    Parameters
    ----------
    forces : list of floats
        Liste avec les valeurs des forces.
    aires : list of floats
        Liste avec les valeurs des aires totales.

    Returns
    -------
    None.

    """
    plt.plot(forces, aires)
    plt.xlabel('Force (N)')
    plt.ylabel('A\u1D3F (m²)')
    # plt.yscale('log')
    # plt.xscale('log')
    # Définir la plage des valeurs des forces et des aires pour le zoom
    # plt.xlim(forces[0], forces[7500])
    # plt.ylim(aires[0], aires[7500])
    plt.savefig("images/loi.png")  # Permet de sauvegarder le fichier
    plt.close()


def superposer_lois(listes, points=None):
    """
    Superpose différentes lois et points.

    Parameters
    ----------
    *listes : tuples of list of floats
        Chaque tuple contient deux listes : la premiere avec les valeurs des
        forces, et la deuxieme avec les valeurs des aires.
    points : list of tuples, optional
        Liste de tuples contenant les coordonnées des points particuliers à
        afficher. Chaque tuple doit avoir deux valeurs : (force, aire).

    Returns
    -------
    None.

    """
    couleurs = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Liste de couleurs
    for i in range(len(listes)):
        forces, aires = listes[i]
        plt.plot(forces, aires, label=f'Loi {i + 1}',
                 color=couleurs[i % len(couleurs)])

    if points:
        points_forces, points_aires = zip(*points)
        plt.scatter(points_forces, points_aires, color='red',
                    marker='x', label='Points recherchés')
    plt.legend()
    plt.xlabel('Force (N)')
    plt.ylabel('Aire (m²)')
    plt.yscale('log')
    plt.xscale('log')
    plt.title('Superposition de lois force-aire')
    plt.savefig("images/superposition_lois.png")
    plt.close()


def superposer_loi_points(forces, aires, points, generation, individu_score,
                          n=None):
    """
    Superpose une loi avec les points a atteindre.

    Parameters
    ----------
    forces : list of floats
        Liste avec les valeurs des forces.
    air Numero de la generation.
    indes : list of floats
        Liste avec les valeurs des aires totales.
    points : list of couple of floats
        Liste des points (force, aire) a atteindre.
    generation : integer
        Numero de la generation.
    individu_score : float
        Score de l'individu lie a la loi.
    n : integer
        Numero du test de l'algorithme.

    Returns
    -------
    None.

    """
    plt.plot(forces/(10**12), aires/(10**12), color="b")

    # map applique la fonction liste a chaque tuple renvoye par zip
    points_forces, points_aires = map(np.array, zip(*points))
    plt.scatter(points_forces/(10**12), points_aires/(10**12), color='red',
                marker='x', label='Points recherchés')

    plt.xlabel('Force (N)')
    plt.ylabel('Aire (m²)')
    plt.title("Génération " + str(generation)
              + " Score " + str(round((individu_score), 5)))
    plt.savefig("images/loi_generation" + str(n) + ".png")
    plt.close()


def superposer_lois_degrade(listes, points=None):
    """
    Superpose différentes lois et points.

    Parameters
    ----------
    *listes : tuples of list of floats
        Chaque tuple contient deux listes : la premiere avec les valeurs des
        forces, et la deuxieme avec les valeurs des aires.
    points : list of tuples, optional
        Liste de tuples contenant les coordonnées des points particuliers à
        afficher. Chaque tuple doit avoir deux valeurs : (force, aire).

    Returns
    -------
    None.

    """
    # Créer une échelle de couleurs allant du bleu clair au bleu foncé
    couleurs = plt.cm.Blues(np.linspace(0.2, 1, len(listes)))

    for i in range(len(listes)):
        forces, aires = listes[i]
        plt.plot(forces, aires, label=f'Loi {i + 1}',
                 color=couleurs[i])

    if points:
        points_forces, points_aires = zip(*points)
        plt.scatter(points_forces, points_aires, color='red',
                    marker='x', label='Points recherchés')

    plt.xlabel('Force (N)')
    plt.ylabel('Aire (m²)')
    plt.title('Superposition de lois force-aire')
    plt.savefig("images/superposition_lois.png")
    plt.close()


def hauteur(hauteurs, n=None):
    """
    Cree l'histogramme des hauteurs.

    Parameters
    ----------
    hauteurs : list of floats
        Liste des hauteurs.
    n : integer
        Numero du test de l'algorithme.

    Returns
    -------
    None.

    """
    N = 121  # Nombre de barres plus 1
    hauteur_max = np.max(hauteurs)  # Hauteur maximale
    bins = [i*hauteur_max/N for i in range(N+1)]  # Bornes des barres
    plt.hist(hauteurs, bins)
    plt.xlabel('Hauteur (\u03BCm)')
    plt.ylabel("Nombre d'occurences")
    plt.savefig("images/hauteurs" + str(n) + ".png")  # Permet de sauvegarder
    plt.close()


def score(scores, n=None):
    """
    Trace l'evolution du score en fonction de la generation.

    Parameters
    ----------
    scores : list of floats
        Liste des scores.
    n : integer
        Numero du test de l'algorithme.

    Returns
    -------
    None.

    """
    plt.plot([i for i in range(len(scores))], scores)
    plt.xlabel('Génération')
    plt.ylabel('Score')
    plt.savefig('images/scores' + str(n) + '.png')
    plt.close()


def score_log(scores):
    """
    Trace l'evolution du score en fonction de la generation en échelle log.

    Parameters
    ----------
    scores : list of floats
        Liste des scores.

    Returns
    -------
    None.

    """
    plt.plot([i for i in range(len(scores))], scores)
    plt.xlabel('Génération')
    plt.ylabel('Score')
    plt.yscale('log')
    if len(scores) == 100:
        plt.savefig('images/scores_log.png')
    plt.close()


def superposer_loi_points_normalise(forces, aires, points, generation,
                                    individu_score):
    """
    Superpose une loi avec les points a atteindre.

    Parameters
    ----------
    forces : list of floats
        Liste avec les valeurs des forces.
    aires : list of floats
        Liste avec les valeurs des aires totales.
    points : list of couple of floats
        Liste des points (force, aire) a atteindre.
    generation : integer
        Numero de la generation.
    individu_score : float
        Score de l'individu lie a la loi.

    Returns
    -------
    None.

    """
    aire_0 = points[-1][1]  # Aire pour normalisee
    force_0 = points[-1][0]  # Force pour normalisee
    plt.plot(forces/force_0, aires/aire_0, color="b")
    # map applique la fonction liste a chaque tuple renvoye par zip
    points_forces, points_aires = map(np.array, zip(*points))
    plt.scatter(points_forces/force_0, points_aires/aire_0, color='red',
                marker='x', label='Points recherchés')

    plt.xlabel('P/P\u2080')
    plt.ylabel('A/A\u2080')
    plt.title("Génération " + str(generation)
              + " Score " + str(round((individu_score), 5)))
    plt.savefig("images/superposition_lois.png")
    plt.close()


if __name__ == "__main__":
    matrice_aire = np.array([[random.random()/10**6 for i in range(5)]
                             for j in range(5)])
    spheres(matrice_aire)
