# Exercice 8 - Partie C : évolution de l'alcoolémie d'Alice

import numpy as np
import matplotlib.pyplot as plt

k1 = 0.1672    # min-1, trouvé dans la partie A
k2 = 7.25e-5   # mol/L/min, trouvé dans la partie B

# Question 5
d = 0.06
rhoeth = 790   # g/L
C0m = d * rhoeth
Meth = 2 * 12 + 6 * 1 + 16   # g/mol
C0 = C0m / Meth
print("La concentration massique de l'éthanol dans la bière est de {} g/L ".format(C0m))
print("La concentration molaire de l'éthanol dans la bière est de {:0.3f} mol/L ".format(C0))
