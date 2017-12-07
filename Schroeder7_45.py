# P43
# HW8
#
# By Spencer Hatch
# 2017/11/07
#
# Schroeder 7.45

# Need these packages/functions
from scipy.special import comb
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

np.set_printoptions(threshold=np.nan)

import scipy.integrate as integrate
import scipy.special as special


T = np.array([1500, 1.5e7])
Pressure = 8. * math.pi**5 / 45 * (1.381e-23 * T)**4. / (6.626e-34 * 3.0e8)**3.

mH = 1.007 * 1.661e-27          # kg
rho = 1e5                       # kg/m^3

NperV = rho / mH

PHydro = NperV * 1.381e-23 * T[1]

print ''
it = np.nditer(Pressure, flags=['f_index'])
while not it.finished:
    print "P,T : %.02e Pa, %.02e K" % (it[0], T[it.index])
    it.iternext()

print 'P_Hydrogen(sun center): %.02e' % PHydro
print 'P_(light)/P_Hydro: %.02e' % (Pressure[1] / PHydro)
