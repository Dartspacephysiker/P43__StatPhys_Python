# P43
# HW6
#
# By Spencer Hatch
# 2017/10/26
#
# Problem 6.34 in Schroeder

# Need these packages/functions
import pdb
from scipy.special import comb
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import scipy.integrate as integrate
import scipy.special as special


figSize = (9, 7)                # in inches

# Use TeX to make plot labels?
useTeX = 1
# To TeX, or not to Tex …
if useTeX:
    import matplotlib
    from matplotlib import rc
    matplotlib.interactive(True)

# Consts
Rgas = 8.315                    # J/mol-K
CtoK = 273.15                   # Deg-C to K
k = 1.381e-23                   # J/K

amutokg = 1.661e-27  # amu to kg (duh)
mN2 = 14.00674 * 2   # N2 mass (amu)

massArr = [r'N$_2$']

ms = np.array([mN2]) * amutokg

vArr = np.arange(10, 2.e3, 10)                                       # m/s
vArr2 = vArr**2

Ts = np.array([300, 600])  # kelvin

distArr = np.empty((0, vArr.size))
mostLikeSpeedArr = np.zeros(Ts.size)
iter = np.nditer(Ts, flags=['f_index'])
# print 'Probability of particle exceeding %.3e km/s' % (ingrerSpeed / 1e3)
while not iter.finished:
    tmpInd = iter.index
    tmpT = iter[0]
    mOver2kT = ms[0] / (2 * k * tmpT)
    const = np.power(mOver2kT / math.pi, 1.5) * 4 * math.pi
    tmpDist = const * vArr2 * np.exp(-mOver2kT * vArr2)
    distArr = np.vstack((distArr, tmpDist))
    mostLikeSpeedArr[tmpInd] = math.sqrt(2 * k * tmpT / ms[0])
    iter.iternext()

# Now plots

# Set up TeXness
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    xLabel = r'$v$ (km/s)'
    yLabel = r'$\mathcal{D}(v)$'
    PTitle = r'Maxwell Speed Distribution for Nitrogen (N$_2$)'

fig = plt.figure(num=0, figsize=figSize)
line0, = plt.plot(
    vArr / 1000, distArr[0, ], label=r'$T =$~%d K ($v_\mathrm{max}$ = %d m/s)' % (Ts[0], mostLikeSpeedArr[0]))
line1, = plt.plot(
    vArr / 1000, distArr[1, ], label=r'$T =$~%d K ($v_\mathrm{max}$ = %d m/s)' % (Ts[1], mostLikeSpeedArr[1]))
# line2, = plt.plot(vArr / 1000, distArr[2, ], label=massArr[2])
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(yLabel, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(PTitle, fontsize=18)
# plt.title(" ".join((PTitle, r'($T =$~%d K)' % Ts[0])), fontsize=18)

# Create legends
leg0 = plt.legend(handles=[line0, line1], loc=1, fontsize=18)
ax = plt.gca().add_artist(leg0)

plt.show()
