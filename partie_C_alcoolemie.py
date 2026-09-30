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

# Question 7
cmax = c.max()
print("La valeur de concentration en éthanol maximale d'Alice est de {:0.4f} mol/L".format(cmax))

# Question 8
tmax = t[c.argmax()]

print("\n=== Question 8 ===\n")
print("L'instant auquel la concentration en éthanol est maximale dans le sang d'Alice est t = {:0.1f} min\n".format(tmax))

# Question 9
# la limite légale est de 0,5 g/L, on la convertit en mol/L pour la comparer à c
Climmass = 0.5   # g/L
Climmol = Climmass / Meth

print("=== Question 9 ===\n")
print("Limite légale : {} g/L, soit {:0.4f} mol/L".format(Climmass, Climmol))
print("Alcoolémie maximale d'Alice : {:0.4f} mol/L, soit {:0.2f} g/L\n".format(cmax, cmax * Meth))
if cmax > Climmol:
    print("Conclusion : Alice n'a pas le droit de conduire à ce moment là\n")
else:
    print("Conclusion : Alice a le droit de conduire à ce moment là\n")

# Question 10
# premier instant après le maximum où l'alcoolémie repasse sous la limite
condition = (t > tmax) & (c < Climmol)
tok = t[condition][0]

print("=== Question 10 ===\n")
print("Le temps au bout duquel Alice aura le droit de prendre le volant est t = {:0.1f} min (soit {:0.1f} h)".format(tok, tok / 60))
