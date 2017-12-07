# P43
# HW6
#
# By Spencer Hatch
# 2017/10/26
#
# Problem 6.39 in Schroeder

# Need these packages/functions
import pdb
from scipy.special import comb
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import scipy.integrate as integrate
import scipy.special as special


def integrand(v, mass, T):
    k = 1.381e-23                   # J/K
    mOver2kT = mass / (2 * k * T)
    const = np.power(mOver2kT / math.pi, 1.5) * 4 * math.pi
    tmpDist = const * v**2 * np.exp(-mOver2kT * v**2)
    return tmpDist


def integNorm(x):
    tmpDist = 4 / math.sqrt(math.pi) * x**2 * np.exp(-x**2)
    return tmpDist


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
mH2 = 1.00794 * 2    # H2 mass (amu)
mHe = 4.002602       # He mass (amu)

massArr = [r'N$_2$', r'H$_2$', r'He']

ms = np.array([mN2, mH2, mHe]) * amutokg

vArr = np.arange(10, 1.2e4, 50)                                       # m/s
vArr2 = vArr**2

Ts = np.array([1000])  # kelvin

ingrerSpeed = 1.1e4                  # m/s

distArr = np.empty((0, vArr.size))
integArr = np.zeros(ms.size)
integNormArr = np.zeros(ms.size)
mostLikeSpeedArr = np.zeros(ms.size)
ms_it = np.nditer(ms, flags=['f_index'])
print 'Probability of particle exceeding %.3e km/s' % (ingrerSpeed / 1e3)
while not ms_it.finished:
    tmpInd = ms_it.index
    tmpm = ms_it[0]
    mOver2kT = tmpm / (2 * k * Ts)
    const = np.power(mOver2kT / math.pi, 1.5) * 4 * math.pi
    tmpDist = const * vArr2 * np.exp(-mOver2kT * vArr2)
    distArr = np.vstack((distArr, tmpDist))
    mostLikeSpeedArr[tmpInd] = math.sqrt(2 * k * Ts / tmpm)
    ingrer = (integrate.quad(integrand, ingrerSpeed,
                             np.inf, args=(tmpm, Ts)))[0]
    ingrNorm = (integrate.quad(
        integNorm, ingrerSpeed / mostLikeSpeedArr[tmpInd], np.inf))[0]
    print '%s: %.3e%% (vmax = %.3e m/s)' % (massArr[tmpInd], ingrer * 100, mostLikeSpeedArr[tmpInd])
    print '%s: %.3e%% (vmax = %.3e m/s)' % (massArr[tmpInd], ingrNorm * 100, mostLikeSpeedArr[tmpInd])
    # np.append(integArr, ingrer)
    integArr[tmpInd] = ingrer
    ms_it.iternext()

# Now plots

# Set up TeXness
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    xLabel = r'$v$ (km/s)'
    yLabel = r'$\mathcal{D}(v)$'
    PTitle = r'Maxwell speed dist'

fig = plt.figure(num=0, figsize=figSize)
line0, = plt.plot(vArr / 1000, distArr[0, ], label=massArr[0])
line1, = plt.plot(vArr / 1000, distArr[1, ], label=massArr[1])
line2, = plt.plot(vArr / 1000, distArr[2, ], label=massArr[2])
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(yLabel, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(" ".join((PTitle, r'($T =$~%d K)' % Ts[0])), fontsize=18)

# Create legends
leg0 = plt.legend(handles=[line0, line1, line2], loc=1, fontsize=18)
ax = plt.gca().add_artist(leg0)

plt.show()
