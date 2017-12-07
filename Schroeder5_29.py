# P43
# Practice Final
#
# By Spencer Hatch
# 2017/11/14
#
# Schroeder 5.29

# Need these packages/functions
from scipy.special import comb
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

np.set_printoptions(threshold=np.nan)

import scipy.integrate as integrate
import scipy.special as special

Gk = -2443.88 * 1000  # J
Ga = -2442.66 * 1000  # J
Gs = -2440.99 * 1000  # J

Sk = 83.81
Sa = 93.22
Ss = 96.11

deltaT_ka = (Gk - Ga) / (Sk - Sa)
deltaT_ks = (Gk - Gs) / (Sk - Ss)
deltaT_as = (Ga - Gs) / (Sa - Ss)

print ''
print 'Kyanite -> andalusite crossover T: %.02f' % (deltaT_ka + 300.)
print 'Kyanite -> sillimanite crossover T: %.02f' % (deltaT_ks + 300.)
print 'andalusite -> sillimanite crossover T: %.02f' % (deltaT_as + 300.)
