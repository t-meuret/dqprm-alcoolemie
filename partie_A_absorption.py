# Exercice 8 - Partie A : absorption de l'alcool dans l'estomac

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# Question 1
c10 = 1 / 0.250   # 1 mole d'éthanol dans 250 mL
print("La concentration initiale d'alcool dans l'estomac est de", c10, "mol/L")

t1 = np.array([0, 1.73, 2.8, 5.5, 18, 22])
c1 = np.array([c10, 3.0, 2.5, 1.6, 0.2, 0.1])

# si la réaction est d'ordre 1, ln(c1/c10) = -k1*t est une droite
lr = scipy.stats.linregress(t1, np.log(c1 / c10))
k1 = -lr.slope
print("Le coefficient de corrélation vaut {:0.6f}".format(abs(lr.rvalue)))
print("La constante de vitesse de la réaction d'absorption vaut k1 = {:0.4f} min-1".format(k1))

plt.plot(t1, np.log(c1 / c10), 'o', label="mesures")
plt.plot(t1, lr.intercept + lr.slope * t1, label="régression linéaire")
plt.xlabel("t (min)")
plt.ylabel("ln(c1/c10)")
plt.legend()
plt.grid()
plt.show()
