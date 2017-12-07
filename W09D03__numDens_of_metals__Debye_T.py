# 2017/11/08
#
# Elem		Density (g/cm^3)	Atomic mass (amu)
# 13 Al		2.70			26.9815
# 29 Cu		8.96			63.546
# 26 Fe		7.86			55.845
# 6 C (di)	3.513			12.0107
# 82 Pb		11.34			207.2

# Need these packages/functions
from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt
import math

# Use TeX to make plot labels?
useTeX = 0

h = 6.626e-34                   # J-s
k = 1.381e-23                   # J/K
const = h / 2 / k * math.pow(6. / math.pi, 1. / 3.)

navn = [r'Al', r'Cu', r'Fe', r'C (diam)', r'Pb']
amutokg = 1.661e-27                                                # kg
dens = np.array([2.7, 8.96, 7.86, 3.513, 11.34]) * 0.001 * 1e6  # kg/m^3
atomicMass = np.array([26.9815, 63.546, 55.845, 12.0107, 207.2])  # amu
c_s = np.array([5100., 3560., 5130., 12000., 1322.])  # m/s

numDens = dens / (atomicMass * amutokg)

# Debye temperature
T_D = const * np.power(numDens, 1. / 3.) * c_s

print ''
print '%-12s: %12s %12s' % ('Elem', 'N dens', 'T_Debye (K)')
it = np.nditer(dens, flags=['f_index'])
while not it.finished:
    print '%-12s: %12.04e %12.03f' % (navn[it.index], numDens[it.index], T_D[it.index])
    it.iternext()
