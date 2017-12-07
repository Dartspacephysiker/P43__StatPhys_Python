# P43
# Final
#
# By Spencer Hatch
# 2017/11/16
#
# Schroeder 5.23

# Need these packages/functions
from scipy.special import comb
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

np.set_printoptions(threshold=np.nan)

import scipy.integrate as integrate
import scipy.special as special


def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx


figSize = (11, 7)                # in inches

saveFig = 1
fname = '/home/spencerh/Desktop/PHYS_43/problems/finalp2_Schroeder5_23.png'
fname1 = '/home/spencerh/Desktop/PHYS_43/problems/finalp2_Schroeder5_23__chemPot.png'
# Use TeX to make plot labels?
useTeX = 1
# To TeX, or not to Tex …
if useTeX:
    import matplotlib
    from matplotlib import rc
    matplotlib.interactive(True)

h = 6.626e-34                   # J-s
T = 5800                        # K
k = 1.381e-23                  # J/K
k_eV = 8.617e-5                    # eV/K
NperV = 2e19                    # m^-3
elecMass = 9.1e-31              # kg

vQ = np.power(h / np.sqrt(2 * math.pi * k * T * elecMass), 3)
mu = - k_eV * T * np.log(1. / NperV / vQ)

Uocc = -13.6                    # eV
Uunocc = 0.                     # eV

Phiocc = Uocc - mu
Phiunocc = Uunocc

print ''
print 'vQ:  %.03e (m^3)' % vQ
print 'mu:  %.03e (eV)' % mu
print ''
print 'Phi (occupied  ): %.02e eV' % Phiocc
print 'Phi (unoccupied): %.02e eV' % Phiunocc

###############################
# PLOT STUFF
###############################

Tarr = np.logspace(1, 5)       # K

vQarr = np.power(h / np.sqrt(2 * math.pi * k * Tarr * elecMass), 3)
muarr = - k_eV * Tarr * np.log(1. / NperV / vQarr)

PhiOccArr = Uocc - muarr
PhiUnoccArr = PhiOccArr * 0.

print ''
print 'Crossover T: %.02f K' % Tarr[find_nearest(PhiOccArr - PhiUnoccArr, 0)]

# Set up TeXness
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    xLabel = r'$T$ (K)'
    y0Label = r'$\Phi$'
    y1Label = r'$\mu$ (eV)'
    P0Title = r'Grand free potential $\Phi$ for $N/V$ = 2e19/m$^3$'
    P1Title = r'Chemical potential for electron ideal gas'

fig0 = plt.figure(num=0, figsize=figSize)
plt.clf()
# line01, = plt.plot(Tarr, mu,label=r'$\Phi_\textrm{occ}$')
line01, = plt.semilogx(Tarr, PhiOccArr, label=r'$\Phi_\textrm{occ}$')
line02, = plt.semilogx(Tarr, PhiUnoccArr, label=r'$\Phi_\textrm{unocc}$')
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(y0Label, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(P0Title, fontsize=18)

leg0 = plt.legend(handles=[line01, line02], loc=2, fontsize=18)
ax = plt.gca().add_artist(leg0)

fig1 = plt.figure(num=1, figsize=figSize)
plt.clf()
line11, = plt.semilogx(Tarr, muarr)
line12, = plt.semilogx(Tarr, muarr * 0. - 13.6,
                       label=r'$-13.6$~eV (T = %.0f K)' % Tarr[find_nearest(muarr, -13.6)])
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(y1Label, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(P1Title, fontsize=18)

leg1 = plt.legend(handles=[line12], loc=3, fontsize=18)
ax = plt.gca().add_artist(leg1)

if saveFig:
    print 'saving figure 0 to %s' % fname
    fig0.savefig(fname)
    print 'saving figure 1 to %s' % fname1
    fig1.savefig(fname1)
