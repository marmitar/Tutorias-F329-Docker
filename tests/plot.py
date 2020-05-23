import numpy as np
from matplotlib import pyplot as plt

x = np.arange(10)
y = x**2
plt.plot(x, y)

plt.savefig('image.png')
plt.savefig('image.pdf')

plt.rcParams['text.usetex'] = True
plt.rcParams['pgf.preamble'] = r"""
    \usepackage[portuguese]{babel}
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
"""

plt.title('Gráfico')
plt.savefig('image.pgf')
