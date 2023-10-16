"""Module qui permet l'affichage des sphères."""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.cm import ScalarMappable
import matplotlib.colors as mcolors
import numpy as np
import random


def affichage(liste_x, liste_y, liste_aire):
    """
    Crée le graphique représentant les sphères.

    Parameters
    ----------
    liste_x : list of float
        Liste des coordonnées x des centres des sphères.
    liste_y : list of float
        Liste des coordonnées y des centres des sphères.
    liste_aire : list of float
        Liste des aires des centres des sphères.

    Raises
    ------
    ValueError
        Si les listes ne sont pas de même taille.

    Returns
    -------
    None.

    """
    # On vérifie que les listes sont de même taille
    if not (len(liste_x) == len(liste_y) and len(liste_y) == len(liste_aire)):
        raise ValueError("Les tailles des listes sont différentes !")

    fig, ax = plt.subplots()  # Crée le graphique

    cmap = plt.get_cmap('viridis')  # Choix du jeu de couleurs
    norm = mcolors.Normalize(vmin=min(liste_aire), vmax=max(liste_aire))
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Permet l'utilisation d'une colorbar

    rayon_max = np.sqrt(liste_aire[0]/np.pi)  # On va chercher le rayon maximal
    for i in range(len(liste_x)):  # Création des cercles
        color = cmap(norm(liste_aire[i]))  # Choix de la couleur du cercle i
        rayon = np.sqrt(liste_aire[i]/np.pi)  # Calcule le rayon
        circle = Circle((liste_x[i], liste_y[i]), radius=rayon,
                        fill=True, color=color)  # Crée le cercle i
        ax.add_patch(circle)  # Ajout du cercle
        if rayon > rayon_max:  # Si le rayon i est supérieur au rayon max
            rayon_max = rayon  # On met à jour le rayon max

    cbar = plt.colorbar(sm, ax=ax)  # Ajoute la colorbar
    cbar.set_label('A\u1D3F (m²)')  # Titre de la colorbar

    # Limites des axes vallent les positions extrêmes décalées du rayon max
    ax.set_xlim(min(liste_x) - rayon_max, max(liste_x) + rayon_max)
    ax.set_ylim(min(liste_y) - rayon_max, max(liste_y) + rayon_max)

    # Affichez le graphique
    plt.axis('scaled')  # Permet un repère normé
    plt.xlabel('x (m)')  # Nom de l'axe x
    plt.ylabel('y (m)')  # Nom de l'axe y
    plt.savefig("aire.png")  # Permet de sauvegarder le fichier
    plt.show()  # Affiche le graphique


if __name__ == "__main__":
    liste_x = ([0.001] * 5 + [0.003] * 5 + [0.005] * 5 + [0.007] * 5
               + [0.009] * 5)
    liste_y = [0.001, 0.003, 0.005, 0.007, 0.009] * 5
    liste_aire = [random.random()/10**6 for i in range(25)]
    affichage(liste_x, liste_y, liste_aire)
