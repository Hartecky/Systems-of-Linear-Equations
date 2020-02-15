from matplotlib import pyplot as plt 
import numpy as np
import matplotlib.patches as mpatches
from scipy.optimize import curve_fit
from scipy import stats

def func(x,a,b):
	return x**a * b

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
#Metoda Cramera
#plt.plot(l_rownan,czas_cramer, 'bo', label='M. Cramera', color='blue')
popt1, pcov1 = curve_fit(func, l_rownan, czas_cramer)
print(popt1)

#Metoda Gaussa
plt.plot(l_rownan,czas_gauss, 'bo', label='M. Gaussa', color='orange')
popt2,pcov2 = curve_fit(func,l_rownan,czas_gauss)
print(popt2)

#Metoda numpy
#plt.plot(l_rownan,czas_numpy, 'bo', label='Numpy solve', color='green')
popt3,pcov3 = curve_fit(func,l_rownan,czas_numpy)
print(popt3)

xfit = np.arange(0, 1100, 0.01)
plt.plot(xfit, func(xfit, *popt1), 'blue', label='fit params: a=%5.3e, b=%5.3e' % tuple(popt1))
plt.plot(xfit, func(xfit, *popt2), 'orange', label='fit params: a=%5.3e, b=%5.3e' % tuple(popt2))
plt.plot(xfit, func(xfit, *popt3), 'green', label='fit params: a=%5.3e, b=%5.3e' % tuple(popt3))

plt.xlabel("Liczba równań")
plt.ylabel("Czas operacji [s]")
plt.legend()
plt.show()

#Cramer
slope, intercept, r_value, p_value, std_err = stats.linregress(czas_cramer,l_rownan)
#Gauss
slope, intercept, r_value, p_value, std_err = stats.linregress(czas_gauss,l_rownan)
