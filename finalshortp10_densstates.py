# P43
# Final
#
# By Spencer Hatch
# Updated 2017/11/06
#
# Based on Schroeder 7.34

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

saveFig = 0
fname7_5 = '/home/spencerh/Desktop/PHYS_43/problems/hw8p3_Schroeder7_5d.png'
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
Tarr = np.arange(0., 1000, 0.1)    # in K


# Part (d)
# x = N_c / N_d = Ratio of ionized phosphorus to phosphorus atoms
x = 0.9 * np.sqrt(Tarr - 600)
x[0:4000] = 1.7 * np.sqrt(400. - np.arange(0., 400, 0.1)) - 2

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
# plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(y0Label, fontsize=18)
plt.grid(False)
plt.subplots_adjust(left=0.15)
# plt.title(P0Title, fontsize=18)

plt.gca().get_yaxis().set_visible(False)
plt.gca().get_xaxis().set_visible(False)

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off')  # labels along the bottom edge are off

plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left='off',      # ticks along the bottom edge are off
    right='off',         # ticks along the top edge are off
    labelbottom='off')  # labels along the bottom edge are off

plt.xlim((0, 1000))
plt.ylim((0, 40))

# fig1 = plt.figure(num=1, figsize=figSize)
# plt.clf()
# line11, = plt.plot(Tarr, chemPot_useElec, label=r'$\mu_e$^-$ (T)$')
# # line12, = plt.plot(Tarr, chemPot_useP, label=r'$\mu_P (T)$')
# line13, = plt.plot(
#     # Tarr, (chemPot[-1] - chemPot[0]) / (Tarr[-1] - Tarr[0]) * Tarr, '-.', label=r'ref. line ($\frac{\mu_{\textrm{e}^{-},\textrm{min}} - \mu_{\textrm{e}^-,\textrm{max}}}{300~\textrm{K}} T$)')
#     Tarr, (chemPot_useElec[-1] - chemPot_useElec[0]) / (Tarr[-1] - Tarr[0]) * Tarr + chemPot_useElec[0], '-.', label=r'ref. line')
# plt.xlabel(xLabel, fontsize=18)
# plt.tick_params(labelsize=16)
# plt.ylabel(y1Label, fontsize=18)
# plt.grid(True)
# plt.subplots_adjust(left=0.15)
# plt.title(P1Title, fontsize=18)

# # Create legends
# # leg1 = plt.legend(handles=[line11, line12, line13], loc=1, fontsize=18)
# leg1 = plt.legend(handles=[line11, line13], loc=1, fontsize=18)
# ax = plt.gca().add_artist(leg1)

# fig2 = plt.figure(num=2, figsize=figSize)
# plt.clf()
# line21, = plt.semilogy(Tarr, np.nan_to_num(1 / (x * NdonorperV) / vQelec))
# line22, = plt.semilogy(Tarr, (Tarr * 0 + 1), '--')
# plt.xlabel(xLabel, fontsize=18)
# plt.tick_params(labelsize=16)
# plt.ylabel(r'$(V_c / N) / v_Q$', fontsize=18)
# plt.grid(True)
# plt.subplots_adjust(left=0.15)
# plt.title(P2Title, fontsize=18)

# axes = plt.gca()
# # axes.set_xlim([xmin,xmax])
# axes.set_ylim([1e-1, 1e9])


# fig3 = plt.figure(num=3, figsize=figSize)
# plt.clf()
# # line31, = plt.plot(Tarr, NcperV, label=r'Intrinsic')
# # line32, = plt.plot(Tarr, x * NdonorperV, '-.', label=r'Donor')
# line31, = plt.semilogy(Tarr, NcperV, label=r'Intrinsic')
# line32, = plt.semilogy(Tarr, x * NdonorperV, '-.', label=r'Donor')
# plt.xlabel(xLabel, fontsize=18)
# plt.tick_params(labelsize=16)
# plt.ylabel(r'$N_c/V$ (m$^{-3}$)', fontsize=18)
# plt.grid(True)
# plt.subplots_adjust(left=0.15)
# plt.title(
#     r'Phosphorus-doped silicon: intrinsic and dopant contributions to conduction', fontsize=18)

# # Create legends
# # leg1 = plt.legend(handles=[line11, line12, line13], loc=1, fontsize=18)
# leg3 = plt.legend(handles=[line31, line32], loc=4, fontsize=18)
# ax = plt.gca().add_artist(leg3)
# axes = plt.gca()
# # axes.set_xlim([xmin,xmax])
# axes.set_ylim([1e15, 1e24])

if saveFig:
    print 'saving figure to %s' % fname7_5
    fig0.savefig(fname7_5)
