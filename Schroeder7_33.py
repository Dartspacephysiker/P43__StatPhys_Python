# P43
# HW8
#
# By Spencer Hatch
# 2017/11/07
#
# Schroeder 7.33

# Need these packages/functions
from scipy.special import comb
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

np.set_printoptions(threshold=np.nan)

import scipy.integrate as integrate
import scipy.special as special

figSize = (11, 7)                # in inches

saveFig = 1
fname = '/home/spencerh/Desktop/PHYS_43/problems/hw8p3_Schroeder7_5d.png'
# Use TeX to make plot labels?
useTeX = 1
# To TeX, or not to Tex …
if useTeX:
    import matplotlib
    from matplotlib import rc
    matplotlib.interactive(True)

R = 8.315                       # J/mol-K
k = 1.381e-23
k_eV = 8.617e-5                 # eV/K
# Tarr = np.arange(400, 401, 0.001)    # in K
# Tarr = np.arange(0.1, 300, 0.1)    # in K
Tarr = 300                      # kelvin
amu = 1.661e-27
h = 6.626e-34
N_A = 6.022e23

#
deltaE = 1.11                   # eV (original value for Si!)
# deltaE = 2.31                   # eV

beta = 1. / (k_eV * Tarr)

NdonorperV = 1.e17 * 1e6  # in (Num phosphorus atoms) / cm^3 * cm^3 / m^3
E_ioniz = 0.044                        # in eV

const = np.power(h / np.sqrt(2 * math.pi * k * Tarr * amu), 3)

# A_Si = 28.086

# vQSi = const * np.power(A_Si, -1.5)

elecMass = 9.1e-31
vQelec = np.power(h / np.sqrt(2 * math.pi * k * Tarr * elecMass), 3)

vol = 1e-6                      # 1 cm^3, or 1e-6 m^3

Nc = vol * 2. / vQelec * np.exp(-beta / 2 * deltaE)

print ''
print 'T = %.02e' % Tarr
print 'Quantum vol (m^3): %.02e' % vQelec
print 'N conduction electrons in 1 cc: %.02e' % Nc
print 'eff density of states  in 1 cc: %.02e' % (vol * 2. / vQelec)

# Part (d)
# x = N_c / N_d = Ratio of ionized phosphorus to phosphorus atoms
# x = 1. / NdonorperV / vQP * \
#     np.exp(-beta * E_ioniz) * \
#     (np.sqrt(1. + 4. * np.exp(beta * E_ioniz) * vQP * NdonorperV) - 1.)

# # print ''
# # print 'Phosphorus'
# # print '======'
# # print ''
# # print 'per-ptcl vol (m^3): %.03e' % VperN
# # print 'quantum vol (m^3): %.03e' % vQO2
# # print 'Z_rot: %.03g' % Z_rotO2
# # print 'Z_int: %.03g' % Z_intO2
# # print 'S (J/K): %.04g' % S_O2
# # print 'mu (eV): %.03g' % mu_O2

# # Set up TeXness
# if useTeX:
#     plt.rc('text', usetex=True)
#     plt.rc('font', family='serif')
#     params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
#     plt.rcParams.update(params)
#     xLabel = r'$T$ (K)'
#     yLabel = r'$N_c / N_d$'
#     P0Title = r'Phosphorus-doped silicon: Fraction of conduction electrons per dopant'

# fig0 = plt.figure(num=0, figsize=figSize)
# plt.clf()
# # line00, = plt.plot(Tarr, x)
# # Tarr, x, label=r'$g(\epsilon)$', alpha=0.5)
# line01, = plt.plot(Tarr, x.clip(min=0))
# plt.xlabel(xLabel, fontsize=18)
# plt.tick_params(labelsize=16)
# plt.ylabel(yLabel, fontsize=18)
# plt.grid(True)
# plt.subplots_adjust(left=0.15)
# plt.title(P0Title, fontsize=18)

# if saveFig:
#     print 'saving figure to %s' % fname
#     fig0.savefig(fname)
