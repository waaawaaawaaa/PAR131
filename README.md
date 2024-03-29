# PAR131
Github du PAR 131 :  Optimisation numérique de la topographie de metainterfaces frottantes.

## Table des matières
* [Description du projet](#description-du-projet)
* [Technologies utilisées](#technologies-utilisées)
* [Utilisation](#utilisation)
* [Crédits](#crédits)
* [Statut du projet](#statut-du-projet)

## Description du projet
Ce projet a lieu dans le cadre d'un projet d'application de recherche à l'École centrale de Lyon, au sein du laboratoire de tribologie et dynamique des systèmes (LTDS). Il a pour objectif d'optimiser numériquement la topographie de metainterfaces frottantes. Pour ce faire, nous utilisons un algorithme génétique qui permet la détermination d'une surface avec des aspérités de taille et de hauteurs variables permettant le respect d'une loi de frottement plus ou moins précise.

## Technologies utilisées
- Python - version 3.11.3
- Bibliothèques python : functools, math, matplotlib, multiprocessing, numpy, psutil, random, time

## Utilisation
### Algorithme direct 

Afin d'utiliser notre algortihme direct et de modéliser une loi de frottement à partir d'un design de surface, tout se passe à partir de la ligne 109 du programme 'algo_direct.py'. Les paramètres modifiables sont les valeurs des rayons de courbures ainsi que les hauteurs. Vous pouvez modifiez les tableaux déjà créé par la commande 'rayons_courbure = np.array'. Vous pouvez choisir les répartitions que vous souhaitez. Nous vous conseillons de travailler avec des rayons de courbures proches de 526 ainsi que des hauteurs inférieures à 120 afin de se rapprocher des cas d'utilisation expérimentaux. Il faut aussi que les tableaux aient la même taille. Nous travaillons personnellement avec 1000 aspérités.
Une fois les tableaux renseignés, vous pouvez faire tourner le programme. Il vous affichera deux images : la loi que respecte votre surface ainsi que la répartition des hauteurs que vous lui avez renseignée. 

### Algorithme génétique

Avant d'utiliser l'algorithme génétique à proprement parler, il faut au préalable renseigner le nombre d'aspérité de travail ainsi que la possibilité au programme de changer les rayons de courbures. Cela se choisit dans le programme 'Individu.py' aux lignes 61 et 62. Ensuite vous pouvez vous rendre sur le programme 'genetique.py' et vous rendre à la toute fin. Dans le main, ligne 222, vous devez renseigner les points (Force, Aire) des points de fonctionnement de la loi voulue. Une fois l'algorithme en marche, vous verrez défiler à l'écran le meilleur score de la génération N, la loi possédant le meilleur score à la génération N ainsi que l'évolution du score génération après génération.


## Crédits
Projet réalisé par [Clément CHENU](https://github.com/cchenu/) et [Maxime YUNGMANN](https://github.com/waaawaaawaaa/) sous l'encadrement de Li FU et de Julien SCHEIBERT à Centrale Lyon, au sein du laboratoire de tribologie et dynamique des systèmes (LTDS).

## Statut du projet
Le projet est : en développement
