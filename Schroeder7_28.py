# P43
# Practice Final
#
# By Spencer Hatch
# 2017/11/14
#
# Schroeder 7.28

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
fname = '/home/spencerh/Desktop/PHYS_43/problems/final_Schroeder7_28.png'
# Use TeX to make plot labels?
useTeX = 1
# To TeX, or not to Tex …
if useTeX:
    import matplotlib
    from matplotlib import rc
    matplotlib.interactive(True)

# Tarr = np.arange(1e-3, 1e3, 0.5)    # in T_F
Tarr = np.logspace(-3, 0.5)    # in T_F
# Tarr = np.logspace(

mu = Tarr * np.log(np.exp(1. / Tarr) - 1)

###############################
# PLOT STUFF
###############################

# Set up TeXness
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    xLabel = r'$T / T_F$'
    # y0Label = r'$\mu/k T_F$'
    y0Label = r'$\mu/\epsilon_F$'
    P0Title = r'2D Fermi Gas: Chemical potential'

fig0 = plt.figure(num=0, figsize=figSize)
plt.clf()
# line01, = plt.plot(Tarr, mu)
line01, = plt.semilogx(Tarr, mu)
# line01, = plt.plot(Tarr, mu)
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(y0Label, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(P0Title, fontsize=18)

if saveFig:
    print 'saving figure to %s' % fname
    fig0.savefig(fname)
