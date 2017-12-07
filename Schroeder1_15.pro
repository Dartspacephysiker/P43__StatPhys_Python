kB       = 1.381D-23                  ;J/K
Tair      = 300                       ;kelvin
mPayload = 500                  ;kg
P        = 1.013D5
mAir1mcule = 4.81235D-26

mayic = mPayload*kB*Tair/( mAir1mcule * P)



V = mayic + INDGEN(100)*2

Tballon = Tair / (1.D - mayic/V)

plot = PLOT(V,Tballon,XTITLE="Volume (m!U3!N)",YTITLE="Balloon air temperature (K)",TITLE='Problem 1.15: Minimum T to keep a hot air ballon afloat')
