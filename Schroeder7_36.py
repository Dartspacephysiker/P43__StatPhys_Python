# 2017/11/05
# Schroeder problem 7.36
# Physics 43 – Statistical Physics
# By Spencer Hatch
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

figSize = (11, 7)                # in inches

# Use TeX to make plot labels?
useTeX = 1
# To TeX, or not to Tex …
if useTeX:
    import matplotlib
    from matplotlib import rc
    matplotlib.interactive(True)


# h = 6.626e-34

# mHe3amu = 3.02
# amu2kg = 1.661e-27
# mHe3 = mHe3amu * amu2kg

# N_A = 6.022e23
# molarDens = 1. / (37 * 1e-6)
# Dens = N_A * molarDens

# k = 8.617e-5

# JtoeV = 1.6e-19

# epsFermi = h**2 / 8 / mHe3 * math.pow(3 / math.pi * Dens, 2. / 3.) / JtoeV
# FermiT = epsFermi / k
# CV_coeff = math.pi**2 * k / 2 / epsFermi

muBB = 0.1

EArr = np.arange(0 - muBB, 1 + muBB, 1e-3)

g_EBar = 1.5 * np.sqrt(EArr.clip(min=0))

g_EwithBBarPos = 0.75 * np.sqrt(EArr.clip(min=muBB) -
                                muBB)
g_EwithBBarNeg = 0.75 * np.sqrt(EArr + muBB)
g_EwithBBar = 0.75 * (np.sqrt(EArr + muBB) + np.sqrt(EArr.clip(min=muBB) -
                                                     muBB))
g_EdiffBBar = 0.75 * (np.sqrt(EArr + muBB) - np.sqrt(EArr.clip(min=muBB) -
                                                     muBB))

# S_coeff = math.pi**2 / 2 / FermiT

# Sliq = S_coeff * TArr
# Ssol = (Sliq * 0) + np.log(2)


# print ''
# print '--------'
# print 'Helium 3'
# print '--------'

# print 'Fermi energy (eV): %.02e' % epsFermi
# print 'Fermi T      (K): %.02e' % FermiT
# print 'Fermi C_V coeff (K^-1): %.02e' % CV_coeff

# Set up TeXness
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    xLabel = r'$\epsilon$ ($\epsilon_F$)'
    yLabel = r'$g(\epsilon) / N$'
    P0Title = r'Fermi Gas: Density of States \quad ($\mu_B B =$~%.02f$\epsilon_F$)' % muBB
    P1Title = r'Fermi Gas: Diff \quad ($\mu_B B =$~%.02f$\epsilon_F$)' % muBB

fig0 = plt.figure(num=0, figsize=figSize)
plt.clf()
line00, = plt.plot(
    EArr, g_EBar, label=r'$g(\epsilon)$', alpha=0.5)
line03, = plt.plot(
    EArr, g_EwithBBar, '-.', label=r'$\frac{1}{2}g(\epsilon - \mu_B B)+\frac{1}{2}g(\epsilon + \mu_B B)$')
line01, = plt.plot(
    EArr, g_EwithBBarPos, '--', label=r'$\frac{1}{2}g(\epsilon - \mu_B B)$', alpha=0.7)
line02, = plt.plot(
    EArr, g_EwithBBarNeg, '--', label=r'$\frac{1}{2}g(\epsilon + \mu_B B)$', alpha=0.7)
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(yLabel, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(P0Title, fontsize=18)

# Create legends
leg0 = plt.legend(handles=[line00, line03, line01, line02], loc=2, fontsize=18)
ax = plt.gca().add_artist(leg0)

plt.show()

fig = plt.figure(num=1, figsize=figSize)
plt.clf()
line10, = plt.plot(
    EArr, g_EdiffBBar, '-.', label=r'$\frac{1}{2}g(\epsilon - \mu_B B)+\frac{1}{2}g(\epsilon + \mu_B B)$')
line11, = plt.plot(
    EArr, -g_EwithBBarPos, '--', label=r'$-\frac{1}{2}g(\epsilon - \mu_B B)$', alpha=0.7)
line12, = plt.plot(
    EArr, g_EwithBBarNeg, '--', label=r'$\frac{1}{2}g(\epsilon + \mu_B B)$', alpha=0.7)

plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(yLabel, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(P1Title, fontsize=18)

# Create legends
leg0 = plt.legend(handles=[line10, line11, line12], loc=2, fontsize=18)
ax = plt.gca().add_artist(leg0)
