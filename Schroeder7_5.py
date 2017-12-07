# P43
# HW8
#
# By Spencer Hatch
# Updated 2017/11/06
#
# Schroeder 7.5 and 7.35

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
fname7_5 = '/home/spencerh/Desktop/PHYS_43/problems/hw8p3_Schroeder7_5d.png'
fname7_35 = '/home/spencerh/Desktop/PHYS_43/problems/hw8p3_Schroeder7_35a.png'
fname7_35a = '/home/spencerh/Desktop/PHYS_43/problems/hw8p3_Schroeder7_35ValidityOfIdealGas.png'
fname7_35c = '/home/spencerh/Desktop/PHYS_43/problems/hw8p3_Schroeder7_35Contributions.png'
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
Tarr = np.arange(1., 1000, 0.5)    # in K
P = 1.013e5                     # Pascals
amu = 1.661e-27
h = 6.626e-34
N_A = 6.022e23

beta = 1. / (k_eV * Tarr)

NdonorperV = 1.e17 * 1e6  # in (Num phosphorus atoms)/cm^3 * cm^3/m^3

###############################
# PROBLEM 7.5 STUFF
###############################

E_ioniz = 0.044                        # in eV

const = np.power(h / np.sqrt(2 * math.pi * k * Tarr * amu), 3)

A_P = 30.973762

vQP = const * np.power(A_P, -1.5)

elecMass = 9.1e-31
vQelec = np.power(h / np.sqrt(2 * math.pi * k * Tarr * elecMass), 3)

# Part (d)
# x = N_c / N_d = Ratio of ionized phosphorus to phosphorus atoms
x = 0.5 / NdonorperV / vQelec * \
    np.exp(-beta * E_ioniz) * \
    (np.sqrt(np.nan_to_num(1. + 4 *
                           np.nan_to_num(np.exp(beta * E_ioniz)) * vQelec * NdonorperV)) - 1.)
# ORIGINALSK BELOW, IN WHICH COEFF OF EXP WAS 4, NOT 2. LED TO 2 BEING UPPER BOUND, NOT 1.
# (np.sqrt(1. + 4 * np.exp(beta * E_ioniz) * vQP * NdonorperV) - 1.)

# print ''
# print 'Phosphorus'
# print '======'
# print ''
# print 'per-ptcl vol (m^3): %.03e' % VperN
# print 'quantum vol (m^3): %.03e' % vQO2
# print 'Z_rot: %.03g' % Z_rotO2
# print 'Z_int: %.03g' % Z_intO2
# print 'S (J/K): %.04g' % S_O2
# print 'mu (eV): %.03g' % mu_O2


###############################
# PROBLEM 7.35 STUFF
###############################


chemPot_useElec = -1. / beta * np.log(1. / (x * NdonorperV) / vQelec * 2)
chemPot_useP = -1. / beta * np.log(1. / NdonorperV / vQP * 2)

# Conduction electrons from silicon
deltaE = 1.11                   # eV
NcperV = 2. / vQelec * np.exp(-beta / 2 * deltaE)


print ''
print 'ELECTRONS'
print '---------'
print '%-12s: %.02e' % (r'v_Qmax', np.max(vQelec))
print '%-12s: %.02e' % (r'v_Qmin', np.min(vQelec))
print '%-12s: %.02e' % (r'(V/N) / v_Qmax', np.max(np.nan_to_num(1 / (x * NdonorperV) / vQelec)))
print '%-12s: %.03e' % (r'(V/N) / v_Qmin', np.min(np.nan_to_num(1 / (x * NdonorperV) / vQelec)))


###############################
# PLOT STUFF
###############################

# Set up TeXness
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    xLabel = r'$T$ (K)'
    y0Label = r'$N_c / N_d$'
    y1Label = r'$eV$'
    P0Title = r'Phosphorus-doped silicon: Fraction of conduction electrons per dopant'
    P1Title = r'Phosphorus-doped silicon: Chemical potential'
    P2Title = r'Phosphorus-doped silicon: Validity of "ideal gas" electrons'

fig0 = plt.figure(num=0, figsize=figSize)
plt.clf()
# line00, = plt.plot(Tarr, x)
# Tarr, x, label=r'$g(\epsilon)$', alpha=0.5)
line01, = plt.plot(Tarr, x.clip(min=0))
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(y0Label, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(P0Title, fontsize=18)

fig1 = plt.figure(num=1, figsize=figSize)
plt.clf()
line11, = plt.plot(Tarr, chemPot_useElec, label=r'$\mu_e$^-$ (T)$')
# line12, = plt.plot(Tarr, chemPot_useP, label=r'$\mu_P (T)$')
line13, = plt.plot(
    # Tarr, (chemPot[-1] - chemPot[0]) / (Tarr[-1] - Tarr[0]) * Tarr, '-.', label=r'ref. line ($\frac{\mu_{\textrm{e}^{-},\textrm{min}} - \mu_{\textrm{e}^-,\textrm{max}}}{300~\textrm{K}} T$)')
    Tarr, (chemPot_useElec[-1] - chemPot_useElec[0]) / (Tarr[-1] - Tarr[0]) * Tarr + chemPot_useElec[0], '-.', label=r'ref. line')
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(y1Label, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(P1Title, fontsize=18)

# Create legends
# leg1 = plt.legend(handles=[line11, line12, line13], loc=1, fontsize=18)
leg1 = plt.legend(handles=[line11, line13], loc=1, fontsize=18)
ax = plt.gca().add_artist(leg1)

fig2 = plt.figure(num=2, figsize=figSize)
plt.clf()
line21, = plt.semilogy(Tarr, np.nan_to_num(1 / (x * NdonorperV) / vQelec))
line22, = plt.semilogy(Tarr, (Tarr * 0 + 1), '--')
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(r'$(V_c / N) / v_Q$', fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(P2Title, fontsize=18)

axes = plt.gca()
# axes.set_xlim([xmin,xmax])
axes.set_ylim([1e-1, 1e9])


fig3 = plt.figure(num=3, figsize=figSize)
plt.clf()
# line31, = plt.plot(Tarr, NcperV, label=r'Intrinsic')
# line32, = plt.plot(Tarr, x * NdonorperV, '-.', label=r'Donor')
line31, = plt.semilogy(Tarr, NcperV, label=r'Intrinsic')
line32, = plt.semilogy(Tarr, x * NdonorperV, '-.', label=r'Donor')
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(r'$N_c/V$ (m$^{-3}$)', fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(
    r'Phosphorus-doped silicon: intrinsic and dopant contributions to conduction', fontsize=18)

# Create legends
# leg1 = plt.legend(handles=[line11, line12, line13], loc=1, fontsize=18)
leg3 = plt.legend(handles=[line31, line32], loc=4, fontsize=18)
ax = plt.gca().add_artist(leg3)
axes = plt.gca()
# axes.set_xlim([xmin,xmax])
axes.set_ylim([1e15, 1e24])

if saveFig:
    print 'saving figure to %s' % fname7_5
    fig0.savefig(fname7_5)
    print 'saving figure to %s' % fname7_35
    fig1.savefig(fname7_35)
    print 'saving figure to %s' % fname7_35a
    fig2.savefig(fname7_35a)
    print 'saving figure to %s' % fname7_35c
    fig3.savefig(fname7_35c)
