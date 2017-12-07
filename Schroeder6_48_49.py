# P43
# HW7
#
# By Spencer Hatch
# 2017/10/27
#
# Problems 6.48 and 6.49 in Schroeder

# Need these packages/functions
from scipy.special import comb
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import scipy.integrate as integrate
import scipy.special as special

R = 8.315                       # J/mol-K
k = 1.381e-23
k_eV = 8.617e-5                 # eV/K
T = 300
P = 1.013e5                     # Pascals
amu = 1.661e-27
h = 6.626e-34
N_A = 6.022e23

VperN = k * T / P
Z_eO2 = 3                         # for O_2
Z_eN2 = 1                         # for N_2

epsilonO2 = 1.8e-4                        # in eV
epsilonN2 = 2.5e-4                        # in eV

const = math.pow(h / math.sqrt(2 * math.pi * k * T * amu), 3)

A_O2 = 15.994 * 2
A_N2 = 14.00674 * 2

Z_rotO2 = k_eV * T / 2 / epsilonO2
Z_rotN2 = k_eV * T / 2 / epsilonN2

Z_intO2 = Z_eO2 * Z_rotO2
Z_intN2 = Z_eN2 * Z_rotN2

vQO2 = const * math.pow(A_O2, -1.5)
vQN2 = const * math.pow(A_N2, -1.5)

T_QMO2 = h**2 / (2 * math.pi * k * amu * A_O2 * math.pow(VperN, 2. / 3.))
T_QMN2 = h**2 / (2 * math.pi * k * amu * A_N2 * math.pow(VperN, 2. / 3.))
T_QMN2 = h**2 / (2 * math.pi * k * amu * A_N2 *
                 math.pow(math.pow(1, 3) * VperN, 2. / 3.))

S_O2 = R * (math.log(VperN * Z_intO2 / vQO2) + 7 / 2)
mu_O2 = -k_eV * T * math.log(VperN * Z_intO2 / vQO2)

S_N2 = R * (math.log(VperN * Z_intN2 / vQN2) + 7 / 2)
mu_N2 = -k_eV * T * math.log(VperN * Z_intN2 / vQN2)

UintN2 = R * T
U_N2 = UintN2 + 1.5 * R * T
H_N2 = U_N2 + R * T
F_N2 = U_N2 - T * S_N2
G_N2 = H_N2 - T * S_N2

print ''
print 'Oxygen'
print '======'
print ''
print 'per-ptcl vol (m^3): %.03e' % VperN
print 'quantum vol (m^3): %.03e' % vQO2
print 'Z_rot: %.03g' % Z_rotO2
print 'Z_int: %.03g' % Z_intO2
print 'S (J/K): %.04g' % S_O2
print 'mu (eV): %.03g' % mu_O2

print ''
print 'Nitrogen'
print '========'
print ''
print 'per-ptcl vol (m^3): %.03e' % VperN
print 'quantum vol (m^3): %.03e' % vQN2
print 'Z_rot: %.03g' % Z_rotN2
print 'Z_int: %.03g' % Z_intN2
print 'S (J/K): %.04g' % S_N2
print 'mu (eV): %.03g' % mu_N2
print 'U (kJ):  %.03g' % (U_N2 / 1000.)
print 'H (kJ):  %.03g' % (H_N2 / 1000.)
print 'F (kJ):  %.03g' % (F_N2 / 1000.)
print 'G (kJ):  %.03g' % (G_N2 / 1000.)
print 'E_avg (eV):  %.03g' % (U_N2 / N_A / 1.6e-19)
print 'E_avg - mu (eV):  %.03g' % ((U_N2 / N_A / 1.6e-19) - mu_N2)
print 'T_QM:  %.03g' % T_QMN2
