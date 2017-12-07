# P43
# HW6
#
# By Spencer Hatch
# 2017/10/23
#
# Exercise 3
# Problems 5.42 and 5.43 in Schroeder

# Need these packages/functions
from scipy.special import comb
import numpy as np
import math
import matplotlib.pyplot as plt

# For part (b)


def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx


# In any case
figSize = (6, 6)                # in inches

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

# Measured latent heats, pressures, and temperatures
Ts = np.array([0, 0.01, 25, 50, 100]) + CtoK  # Kelvin
Ls = np.array([51.07, 45.06, 43.99, 42.92, 40.66])  # kJ/mol
Ps = np.array([0.00611, 0.00612, 0.0317, 0.1234, 1.013])  # bar

# Temperature array

# T limits
# Give these values in deg-C!
Tbot = 0
# Ttop = 100
Ttop = 40

step = 0.01
start = Tbot + CtoK
stop = Ttop + CtoK
T = np.arange(start, stop, step)

# Calculate vapor pressure for each measured value of T, L, and P_v (as recorded in Ts, Ls, and Ps)
# NOTE, divide by np.exp(-((Ls[tmpInd] * 1000) / (Rgas * Ts[tmpInd])) for each iteration to give correct vapor pressure.
Parr = np.empty((0, T.size))
Ts_it = np.nditer(Ts, flags=['f_index'])
while not Ts_it.finished:
    tmpInd = Ts_it.index
    tmpT = Ts_it[0]
    Ptmp = (Ps[tmpInd] / np.exp(-((Ls[tmpInd] * 1000) / (Rgas * Ts[tmpInd])))
            ) * np.exp(-((Ls[tmpInd] * 1000) / (Rgas * T)))
    Parr = np.vstack((Parr, Ptmp))
    Ts_it.iternext()


Tinds = np.searchsorted(Ts, T)
TLinds = (Tinds - 1).clip(min=0)

L = Ls[Tinds]
P = np.zeros(T.size)

# Try to lin interp pressures
T_it = np.nditer(T, flags=['f_index'])
while not T_it.finished:
    tmpInd = T_it.index
    tmpT = T_it[0]
    TLind = TLinds[tmpInd]
    Tind = Tinds[tmpInd]
    T0 = Ts[TLind]
    T1 = Ts[Tind]
    # print "%f <%d>" % (tmpT, tmpInd)
    # print "%f %f %f" % (tmpT, T0, T1)
    if np.isclose(tmpT, T0):
        P[tmpInd] = Parr[TLind, T_it.index]
    elif np.isclose(tmpT, T1):
        P[tmpInd] = Parr[Tind, T_it.index]
    elif tmpT < T1:
        P[tmpInd] = ((T1 - tmpT) * Parr[TLind, T_it.index] +
                     (tmpT - T0) * Parr[Tind, T_it.index]) / (T1 - T0)
    T_it.iternext()

# Now plots

# Set up TeXness
if useTeX:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
    plt.rcParams.update(params)
    xLabel = r'$T$ ($^\circ$C)'
    LLabel = r'$L$ (kJ/mol)'
    LTitle = r'Latent heat for liquid-gas phase transformation of H$_2$O'
    # PLabel = r'$P / P_0$'
    PLabel = r'$P$ (bar)'
    PTitle = r'H$_2$O Vapor Pressure'
# else:
#     yLabel = r'L'

# plt.figure(num=1, figsize=figSize)
# plt.plot(T - CtoK, L)
# plt.xlabel(xLabel, fontsize=16)
# plt.ylabel(LLabel, fontsize=16)
# plt.grid(True)
# plt.xlim((N.min(), N.max()))

# Make room for yLabel
# plt.subplots_adjust(left=0.15)
# plt.title(LTitle, fontsize=16)
# plt.show()

plt.figure(num=2, figsize=figSize)
plt.plot(T - CtoK, P)
plt.xlabel(xLabel, fontsize=16)
plt.ylabel(PLabel, fontsize=16)
plt.grid(True)
plt.subplots_adjust(left=0.15)
plt.title(PTitle, fontsize=16)
plt.show()

# Part (b)
print ""
print "Part (b)"
print ""
Pv_at_30 = P[np.where(np.isclose(T, 30 + CtoK))]

RH = np.array([0.9, 0.4])
print Pv_at_30[0] * RH
indP90 = find_nearest(P, Pv_at_30[0] * RH[0])
indP40 = find_nearest(P, Pv_at_30[0] * RH[1])
print "Vapor pressure, Dew point"
print "%f %f" % (P[indP90], T[indP90] - CtoK)
print "%f %f" % (P[indP90], T[indP40] - CtoK)

# Schroeder 5.43
print ""
print "Schroeder 5.43"
print ""
bodyT = 35                      # in deg-C
bodyRelHum = 0.9
Pv_at_bodyT = P[np.where(np.isclose(T, bodyT + CtoK))]
indP90 = find_nearest(P, Pv_at_bodyT[0] * bodyRelHum)
print "Vapor pressure, Dew point"
print "%f %f" % (P[indP90], T[indP90] - CtoK)
