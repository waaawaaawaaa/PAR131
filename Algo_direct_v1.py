# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:21:16 2023

@author: Maxime
"""
import numpy as np
from math import sqrt as sq
from math import pi
import matplotlib.pyplot as plt
 
def loi_GW(rayon_courbure, lambda_param):
    module_young = 3 * 10^9
    coef_poisson = 0.4
    E_etoile = module_young/(1-coef_poisson*coef_poisson)
    Asp = 64* [0] # 0 si la sphère n'est pas encore atteinte 1 si elle est atteinte
    Hauteur = np.round(np.random.exponential(scale=1/lambda_param, size=64),6) #hauteur répartie aléatoirement
    P=[] #liste des forces
    A=[] #liste des aires

    for i in range (100):
        force = i*0.05
        P.append(force)
        aire_reelle = sq(pi)*sq(rayon_courbure/lambda_param)*(force/E_etoile)
        A.append(aire_reelle)
        
    plt.plot(P, A) 
    plt.xlabel('Force normale appliquée P')
    plt.ylabel('Aire de contact réelle')
    plt.title("Evolution de l'aire en fonction de la force appliquée")
    plt.show()
    