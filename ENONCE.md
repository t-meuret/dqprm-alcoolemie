# Exercice 8 - Evolution de l'alcoolémie au cours du temps

Par définition, on appelle «alcoolémie» la concentration en $g/L$ d'éthanol ($CH_3CH_2OH$) dans le sang d'une personne. En France, la loi interdit à une personne de conduire si son alcoolémie est supérieure à $0.5\ g/L$.

On se propose dans cet exercice d'étudier comment varie l'alcoolémie d'une personne à partir du moment où elle boit deux bières (chacune de $50\ cL$ et à $6\ \\%$), de façon notamment à savoir à quel moment elle pourra prendre le volant.

Il faut pour cela étudier deux mécanismes différents :
* l'**absorption de l'alcool dans le sang**, qui se fait par diffusion à travers les parois de l'estomac et de l'intestin grêle
* l'**élimination de l'alcool contenu dans le sang**, qui est effectuée essentiellement par des enzymes au niveau du foie (grâce à une réaction d'oxydation)

On va étudier chacun de ces deux processus séparément (dans les parties A et B), puis on combinera les deux dans la partie C.

## A - Absorption de l'alcool à travers la paroi stomacale

On cherche dans ce paragraphe à étudier la loi cinétique modélisant le processus d'absorption, c'est à dire que l'on cherche à déterminer son ordre (si elle en possède un) et sa constante de vitesse $k$.

Pour cela, on réalise l'expérience suivante : on fait boire à un homme (initialement à jeun, c'est à dire l'estomac vide) une boisson alcoolisée de volume $V = 250\ mL$ contenant $1\ mole$ d'éthanol. On mesure alors la concentration $c_1$ de l'éthanol dans l'estomac de l'homme en fonction du temps.

Les résultats obtenus sont regroupés dans le tableau ci-dessous :

| $t$ (en min) | 0 | 1,73 | 2,8 | 5,5 | 18 | 22 |
|---|---|---|---|---|---|---|
| $c_1$ (en mol/L) | à déterminer | 3,0 | 2,5 | 1,6 | 0,2 | 0,1 |

**Question 1.** Utiliser ces données pour prouver graphiquement que la réaction d'absorption de l'alcool dans le sang suit une loi cinétique d'ordre $1$, et déterminer sa constante de vitesse $k_1$ (en précisant son unité).

NB. On fera appel pour cela à la fonction [linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) du sous-module `stats` de SciPy.

**Rappel**

Notons $c_1(t)$ la concentration de l'alcool dans l'estomac au cours du temps et $v_1=-\frac{dc_1}{dt}$ la vitesse d'absorption de l'alcool au niveau de la paroi de l'estomac.

Si la réaction est d'ordre 1, on aura aussi $v_1=kc_1(t)$ et $c_1(t)$ sera donc solution de l'équation différentielle :

$$\frac{dc_1(t)}{dt}+kc_1(t)= 0$$

qui se résout immédiatement en :

$$c_1(t) =c_{1,0}.e^{-kt}$$

où $c_{1,0}$ est la concentration initiale.

Ainsi, si la réaction est bien d'ordre 1, on aura :

$$ln(\frac{c_1(t)}{c_{1,0}})=-kt$$

**Question 2.** Calculer la valeur (en minutes) du temps de demi-réaction $t_{1/2,1}$ de la réaction d'absorption de l'alcool dans le sang.

## B - Oxydation de l'alcool dans le sang

Une fois que l'alcool est passé dans le sang, il est progressivement éliminé (surtout au niveau du foie) par une réaction d'oxydation qui le transforme en éthanal. Cette réaction a lieu grâce à une enzyme appelée alcool-déshydrogénase.

On cherche à présent à déterminer la loi de vitesse de cette réaction d'élimination de l'alcool.

Pour cela, on injecte directement (par voie veineuse) une certaine quantité d'alcool dans le sang d'un homme et on mesure par des prélèvements successifs l'évolution de la concentration $c_2$ de l'alcool dans le sang de cet homme au cours du temps (on suppose que l'injection est quasi-instantanée et que la concentration de l'alcool dans le sang est la même en tout endroit du corps). On obtient les données du tableau suivant :

| $t$ (en min) | 0 | 120 | 240 | 360 | 480 | 600 | 720 |
|---|---|---|---|---|---|---|---|
| $c_2$ (en mol/L) | 0,05 | 0,0413 | 0,0326 | 0,0239 | 0,0152 | 0,0065 | 0 |

**Question 3.** A l'aide de ces données, déterminer l'ordre de cette réaction ainsi que sa constante de vitesse $k_2$.

**Question 4.** Calculer en minutes le temps de demi réaction $t_{1/2,2}$ de cette réaction et comparez le au temps de demi-réaction de l'absorption de l'alcool $t_{1/2,1}$. Commentaire ?

## C - Evolution de l'alcoolémie au cours du temps

Maintenant que l'on connaît les lois de vitesse de la réaction d'absorption et de la réaction d'élimination de l'alcool, on peut calculer comment évolue l'alcoolémie (concentration d'alcool dans le sang) au cours du temps, à partir du moment où une personne boit de l'alcool.

Notons $c$ la concentration (en $mol/L$) de l'alcool dans le sang et $v=\frac{dc}{dt}$ la vitesse à laquelle varie cette concentration. On note également $V_s$ le volume total du sang et de l'ensemble des compartiments hydriques de l'organisme (dans lesquels se dissout l'alcool) et $V_e$ le volume de la boisson alcoolisée ingérée par la personne (qui correspond également au volume de son estomac puisqu'on considère que la personne était à jeun avant de boire).

La concentration d'alcool dans le sang à l'instant $t$ s'écrit :

$$c(t)=C_0\frac{V_e}{V_s}(1-e^{-k_1t})-k_2t$$

où $C_0$ est la concentration en alcool dans la boisson alcoolisée.

Lors d'une soirée, Alice boit deux bières, chacune de volume $V_0 = 50\ cL$ et de «degré alcoolique» $d = 6\ \\%$.

**Rappel** : le «degré alcoolique» correspond au pourcentage volumique d'éthanol dans la boisson, c'est à dire que : $d=\frac{V_{ethanol}}{V_{total}}$

**Question 5.** Sachant que l'éthanol a une masse volumique $\rho_{eth}=0,79\ kg/L$, calculer la concentration $C_0$ de l'éthanol dans la bière, en $g/L$ puis en $mol/L$ (on donne les masses molaires : $M_C = 12\ g/mol$, $M_H = 1,0\ g/mol$ et $M_O = 16\ g/mol$).

**Question 6.** Tracer la fonction $c(t)=C_0\frac{V_e}{V_s}(1-e^{-k_1t})-k_2t$ représentant l'évolution de la concentration en éthanol dans le sang d'Alice (en $mol/L$) à partir du moment où elle boit ses deux bières. On prendra $V_s = 40\ L$ comme volume total du sang et des compartiments hydriques dans le corps d'Alice.

**Question 7.** Déterminer la valeur de concentration en éthanol maximale d'Alice.

**Question 8.** Déterminer l'instant $t_{max}$ auquel la concentration en éthanol est maximale dans le sang d'Alice.

**Question 9.** Alice a-t-elle le droit de conduire à ce moment là ?

**Question 10.** Déterminer le temps au bout duquel Alice aura le droit de prendre le volant.
