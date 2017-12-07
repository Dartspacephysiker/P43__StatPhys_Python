# 2017/09/20 This script produces a plot of the relative height of the peak of
# the multiplicity function as a function of number of coins
#
# Shown on week 2, day 3 in P43 class
#
# Number of coins: N
# Number of heads: n
# Multiplicity function peaks at n = N/2 (denoted by variable N2 below)
# We measure height of the peak relative to the multiplicity of the macrostate with
# n = N/4.
# (The relative number of heads is set with variable relN.)

# Need these packages/functions
from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt

# In any case
logPlot = True
figSize = (6, 6)                # in inches
xLabel = r'N Coins'

# Use TeX to make plot labels?
useTeX = 0

# Dataz
step = 5                        # Step between N Coins
NStart = step                   # Initial value of N Coins array
NStop = 100 + step              # Final value of N Coins array
N = np.arange(NStart, NStop, step)  # N Coins array
# n = N / 2                     # N Heads

# Uncomment these if you want to use TeX typesetting
if useTeX:
    import matplotlib
    from matplotlib import rc
    matplotlib.interactive(True)

# Set up TeXness params
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    # yLabel = r'$\log \Big (\binom{N}{N/2} \Big / \binom{N}{N/%s} \Big)$' % step
    if logPlot:
        yLabel = r'$\log \Big (\binom{N}{N/2} \Big / \binom{N}{N/%s} \Big)$' % step
    else:
        yLabel = r'$\binom{N}{N/2} \Big / \binom{N}{N/%s}$' % step
else:
    if logPlot:
        yLabel = r'log ( nCr(N,N/2) / nCr(N,N/4) )'
    else:
        yLabel = r'nCr(N,N/2) / nCr(N,N/4)'

troubleVals = np.where((N % step) != 0)
if len(troubleVals[0]) != 0:
    print r"You might want to make sure that all values of N are integer multiples of your step variable (you picked step=%d)." % step
    print r"Your plot will be funktified otherwise."

# Multiplicities
PeakMultiplicity = comb(N, N / 2)
RelMultiplicity = comb(N, N / step)
ratio = PeakMultiplicity / RelMultiplicity

yVal = np.log10(ratio) if logPlot else ratio

plt.figure(num=1, figsize=figSize)
plt.plot(N, yVal)
plt.xlabel(xLabel, fontsize=16)
plt.ylabel(yLabel, fontsize=16)

plt.grid(True)
# plt.xlim((N.min(), N.max()))

# Make room for yLabel
plt.subplots_adjust(left=0.15)

# plt.savefig('coins')
# plt.show()
