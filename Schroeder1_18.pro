
kB       = 1.381D-23            ;J/K
T        = 300                  ;K

N        = 14.00674
uTokg    = 1.661D-27
N2       = N * 2
N2kg     = N2  * uTokg


vrms     = SQRT(3 * kB * T / N2kg)

;And 1.19
H = 1.00794D
O = 15.9994D

H2 = 2 * H
O2 = 2 * O

dat = SQRT(O2/H2)

PRINT,'diff between vrms,O2 and vrms,H2: ',dat