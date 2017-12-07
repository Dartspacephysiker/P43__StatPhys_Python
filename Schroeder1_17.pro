
kB       = 1.381D-23            ;J/K
N_A      = 6.022D23
R        = kB*N_A

B_of_T   = [-160,-35,-4.2D,9.0D,16.9D,21.3D] ;cm^3/mol, NOT m^3/mol
T        = [100,200,300,400,500,600] ;kelvin
P0       = 1.013D5              ;1 atm in Pa
VperN    = R*T/P0


;convert B_of_T to m^3/mol
B_of_T  *= 1D-6

secondTerm = B_of_T * P0 / R / T

VperNVirial = R*T/P0 * (1 + secondTerm)

M              = R*T/P0
VperNVirialAltPos = (M + SQRT(M^2 + 4 * M * B_of_T))/2.D
VperNVirialAltNeg = (M - SQRT(M^2 + 4 * M * B_of_T))/2.D


pctDiff     = (VperN-VperNVirial)/VperNVirial*100.
pctDiffAlt  = (VperN-VperNVirialAltPos)/VperNVirialAltPos*100.

PRINT,FORMAT='(A0,T15,A0,T30,A0,T45,A0,T60,A0,T80,A0,T110,A0,T125,A0)', $
      "Temperature", $
      "B(T)", $
      '2nd term', $
      "Vol. per mole", $
      "Vol./mole (virial)", $
      "% diff rel. to virial", $
      "Other", $
      "OtherNeg"
FOR k=0,N_ELEMENTS(T)-1 DO PRINT,FORMAT='(I0,T15,G0.3,T30,G0.3,T45,G0.3,T60,G0.3,T80,G0.3,T110,G0.3,T125,G0.3)', $
                                 T[k], $
                                 B_of_T[k], $
                                 secondTerm[k], $
                                 VperN[k], $
                                 VperNVirial[k], $
                                 pctDiff[k], $
                                 VperNVirialAltPos[k], $
                                 pctDiffAlt[k]

;Part d)
T100ind = WHERE(T EQ 100)
T600ind = WHERE(T EQ 600)
a = (B_of_T[T600ind] - B_of_T[T100ind]) / (1. / T[T100ind] / R - 1. / T[T600ind] / R )

b = B_of_T[T100ind] + a / 100 / R
a = a[0]
b = b[0]
;With predictions for a and b, we can do a predicted vs. data

Tarr        = INDGEN(101)*10+100
B_of_T_pred = b - a / R / Tarr

plotPred = PLOT(Tarr, $
                B_of_T_pred, $
                XRANGE=MINMAX(T), $
                NAME='Predicted', $
                ;; SYMBOL='*', $
                ;; LINESTYLE='', $
                XTITLE="Temperature (K)", $
                YTITLE="B(T)", $
                TITLE='Problem 1.17: van der Waals prediction of B(T), and experimentally determined B(T)')


plotObs = PLOT(T, $
               B_of_T, $
               SYMBOL='*', $
               LINESTYLE='', $
               NAME='Actual', $
               /OVERPLOT)


leg = LEGEND(TARGET=[plotPred,plotObs])