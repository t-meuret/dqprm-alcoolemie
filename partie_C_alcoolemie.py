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

# Question 6
V0 = 0.5   # L
Ve = 2 * V0
Vs = 40    # L
t = np.arange(0, 260, 0.5)
c = C0 * Ve / Vs * (1 - np.exp(-k1 * t)) - k2 * t

plt.figure(figsize=(8, 5))
plt.plot(t, c)
plt.xlabel("t (min)")
plt.ylabel("concentration en éthanol dans le sang (mol/L)")
plt.title("Alcoolémie d'Alice après deux bières")
plt.grid()
plt.show()
