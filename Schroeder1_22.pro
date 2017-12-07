kB       = 1.381D-23            ;J/K
T        = 300                  ;K
m        = 4.81235D-26

V        = 0.01                 ;m^3
A        = 1D-6

tau = 2 * V / A / SQRT(kB*T/m)

;part e)
P0       = 60                   ;Initial pressure in psi
Patm     = 1.013D5              ;Atmospheric pressure (final) in pascals
psiToPa  = 6894.75729D          ;pounds/square inch to pascals
VTube    = 100.D * (1.D-6)      ;bike tube volume in cm^3 (to m^3)
Tdeflate = 3600                 ;time to deflation (s)

;; Ahole    = 2 * VTube * Tdeflate / ( ALOG(P0*psiToPa/Patm) * SQRT(kB*T/m) )
Ahole    = 2 * ALOG(P0*psiToPa/Patm)* VTube / ( Tdeflate * SQRT(kB*T/m) )
Aholecm2 = Ahole * 100.^2
rholecm  = SQRT(Aholecm2/!PI)

PRINT,FORMAT='(A0,G0.2,A0)',"Hole radius: ",rholecm," (cm)"


;part f)
;Toss out the dog corpse
Awindow = 0.25                  ;m^2
Topen   = 3                     ;s
Vroom   = 6.^3                  ;m^3

tauScience = 2.D * Vroom / ( Awindow * SQRT(kB * T / m) )

PfOverP0 = EXP(-Topen/tauScience)
PRINT,''
PRINT,FORMAT='(A0,F0.5,A0)',"Pressure reduced to ",PfOverP0," atm, sir!"