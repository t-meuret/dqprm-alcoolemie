# Exercice 8 - Partie B : élimination de l'alcool dans le sang

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# Question 3
t2 = np.array([0, 120, 240, 360, 480, 600, 720])
c2 = np.array([0.05, 0.0413, 0.0326, 0.0239, 0.0152, 0.0065, 0])

# le dernier point (c2 = 0) est exclu : tout l'alcool est éliminé avant 720 min
# (et ln(0) n'est pas défini pour tester l'ordre 1)
# si la réaction est d'ordre 0, c2 = c20 - k2*t est une droite
lr0 = scipy.stats.linregress(t2[:-1], c2[:-1])
# si la réaction est d'ordre 1, ln(c2/c20) = -k*t est une droite
lr1 = scipy.stats.linregress(t2[:-1], np.log(c2[:-1] / c2[0]))
k2 = -lr0.slope

print("=== Question 3 ===\n")
print("Coefficients de corrélation :")
print("  - ordre 0, c2 = f(t)         : |r| = {:0.6f}".format(abs(lr0.rvalue)))
print("  - ordre 1, ln(c2/c20) = f(t) : |r| = {:0.6f}\n".format(abs(lr1.rvalue)))
print("Conclusion : c2 diminue de 0,0087 mol/L toutes les 120 min, la réaction est d'ordre 0\n")
print("La constante de vitesse de la réaction d'élimination vaut k2 = {:0.3e} mol.L-1.min-1\n".format(k2))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t2, c2, 'o', label="mesures")
plt.plot(t2[:-1], lr0.intercept + lr0.slope * t2[:-1], label="régression linéaire")
plt.xlabel("t (min)")
plt.ylabel("c2 (mol/L)")
plt.title("Ordre 0 : c2 = f(t) est une droite")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(t2[:-1], np.log(c2[:-1] / c2[0]), 'o', label="mesures")
plt.plot(t2[:-1], lr1.intercept + lr1.slope * t2[:-1], label="régression linéaire")
plt.xlabel("t (min)")
plt.ylabel("ln(c2/c20)")
plt.title("Ordre 1 : ln(c2/c20) = f(t) n'est pas une droite")
plt.legend()
plt.grid()

plt.show()

# Question 4
# pour une réaction d'ordre 0, c2(t1/2) = c20/2 donc t1/2 = c20 / (2*k2)
tdemi2 = c2[0] / (2 * k2)

# t1/2,1 de la partie A (ordre 1 : t1/2 = ln(2) / k1)
c10 = 1 / 0.250
t1 = np.array([0, 1.73, 2.8, 5.5, 18, 22])
c1 = np.array([c10, 3.0, 2.5, 1.6, 0.2, 0.1])
k1 = -scipy.stats.linregress(t1, np.log(c1 / c10)).slope
tdemi1 = np.log(2) / k1

print("=== Question 4 ===\n")
print("Le temps de demi-réaction vaut t1/2,2 = {:0.1f} min (soit {:0.1f} h)\n".format(tdemi2, tdemi2 / 60))
print("Comparaison : t1/2,2 / t1/2,1 = {:0.1f} / {:0.3f} = {:0.0f}\n".format(tdemi2, tdemi1, tdemi2 / tdemi1))
print("Commentaire :")
print("  - l'élimination est environ {:0.0f} fois plus lente que l'absorption :"
      " c'est elle qui fixe la durée de l'alcoolémie".format(tdemi2 / tdemi1))
print("  - ordre 0 : le foie élimine une quantité fixe d'alcool par unité de temps, quelle que soit la quantité bue")
