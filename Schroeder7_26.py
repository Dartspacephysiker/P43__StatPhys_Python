# 2017/11/04
# Schroeder problem 7.26
# Physics 43 – Statistical Physics
# By Spencer Hatch
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

figSize = (9, 7)                # in inches

# Use TeX to make plot labels?
useTeX = 1
# To TeX, or not to Tex …
if useTeX:
    import matplotlib
    from matplotlib import rc
    matplotlib.interactive(True)


h = 6.626e-34

mHe3amu = 3.02
amu2kg = 1.661e-27
mHe3 = mHe3amu * amu2kg

N_A = 6.022e23
molarDens = 1. / (37 * 1e-6)
Dens = N_A * molarDens

k = 8.617e-5

JtoeV = 1.6e-19

epsFermi = h**2 / 8 / mHe3 * math.pow(3 / math.pi * Dens, 2. / 3.) / JtoeV
FermiT = epsFermi / k
CV_coeff = math.pi**2 * k / 2 / epsFermi

TArr = np.arange(0, 1, 1e-3)                                       # m/s


S_coeff = math.pi**2 / 2 / FermiT

Sliq = S_coeff * TArr
Ssol = (Sliq * 0) + np.log(2)


print ''
print '-0------'
print 'Helium 3'
print '-0------'

print 'Fermi energy (eV): %.02e' % epsFermi
print 'Fermi T      (K): %.02e' % FermiT
print 'Fermi C_V coeff (K^-1): %.02e' % CV_coeff

# Set up TeXness
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    xLabel = r'$T$ (K)'
    yLabel = r'$\frac{S}{Nk}$'
    PTitle = r'$^3$He Entropy'

fig = plt.figure(num=0, figsize=figSize)
line0, = plt.plot(
    TArr, Sliq, label=r'Liquid')
line1, = plt.plot(
    TArr, Ssol, label=r'Solid')
plt.xlabel(xLabel, fontsize=18)
plt.tick_params(labelsize=16)
plt.ylabel(yLabel, fontsize=18)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(PTitle, fontsize=18)

# Create legends
leg0 = plt.legend(handles=[line0, line1], loc=2, fontsize=18)
ax = plt.gca().add_artist(leg0)

plt.show()
