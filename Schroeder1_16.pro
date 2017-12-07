alts = [0,1430,3090,4420,8850,20000] ;m
navn = ['Ogden, Utah','Leadville, Colorado','Mt. Whitney, California','Mt. Everest, Nepal/Tibet']



g        = 9.8                  ;m/s^2
kB       = 1.381D-23            ;J/K
Tair      = 300                 ;kelvin
P0       = 1.013D5              ;1 atm in Pa
mAir1mcule = 4.81235D-26        ;kg

P = P0 * EXP(-mAir1mcule * g / kB / Tair * alts)


plot = PLOT(alts,P, $
            SYMBOL='*', $
            LINESTYLE='', $
            XTITLE="Altitude (m)", $
            YTITLE="Pressure", $
            TITLE='Problem 1.16: Exponential atmosphere')
