from matplotlib import pyplot as plt 
import matplotlib.patches as mpatches
import numpy as np
l_rownan = np.array([50,
100,
150,
200,
250,
300,
500,
600,
700,
800,
1000,
1100
])

czas_cramer = np.array([
0.005142567000802956,
0.034331930000917055,
0.11526559199955955,
0.33505518800120626,
0.7443063360005908,
2.498606536999432,
12.300197139000375,
21.238422148999234,
27.029957020000438,
44.714774731000944,
109.30554160599968,
167.02598880200094
])

czas_gauss = np.array([0.0029755089999525808,
0.009966904999600956,
0.021535487998335157,
0.04106358100034413,
0.05719664899879717,
0.08035564400051953,
0.2769476490029774,
0.38976130100127193,
0.580783371002326,
0.6933282669997425,
1.0908481719998235,
2.0726115268
])

czas_numpy = np.array([0.0015139349998207763,
0.000715161000698572,
0.001206385000841692,
0.001929633999679936,
0.0029084170018904842,
0.004539889003353892,
0.014148624999506865,
0.03508146799867973,
0.035970655000710394,
0.05468122999809566,
0.1014957190000132,
0.14332926600036444
])

cramer = mpatches.Patch(color = 'blue', label = 'Metoda Cramera')
gauss = mpatches.Patch(color="orange", label = 'Metoda Gaussa')
solve = mpatches.Patch(color = "green", label = 'Numpy solve')

plt.plot(l_rownan, czas_cramer, '--', linestyle='dashed', marker='o')
plt.plot(l_rownan, czas_gauss, '--', color='orange',linestyle='dashed', marker='o')
plt.plot(l_rownan, czas_numpy, '--', color='green', marker='o')

plt.title("Graph of the dependence of the number of equations and the time needed to solve it")
plt.xlabel("Number of equations")
plt.ylabel("Time [s]")
plt.legend(handles=[cramer, gauss, solve])
plt.show()