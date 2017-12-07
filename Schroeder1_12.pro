H = 1.00794D
O = 15.9994D
N = 14.00674
Pb = 207.2
Si = 28.0855D
Ar = 39.948D

N_A = 6.022D23
uTokg = 1.661D-27

H2O  = H * 2 + O
N2   = N * 2
SiO2 = Si + O * 2

H2Okg  = H2O  * N_A * uTokg
N2kg   = N2   * N_A * uTokg
Pbkg   = Pb   * N_A * uTokg
SiO2kg = SiO2 * N_A * uTokg

PRINT,FORMAT='("H2O (u)  : ",G0.8)',H2O 
PRINT,FORMAT='("N2 (u)   : ",G0.8)',N2  
PRINT,FORMAT='("Pb (u)   : ",G0.8)',Pb  
PRINT,FORMAT='("SiO2 (u) : ",G0.8)',SiO2
PRINT,''
PRINT,FORMAT='("H2O (mol) : ",G0.8)',H2O * N_A
PRINT,FORMAT='("N2 (mol)  : ",G0.8)',N2  * N_A
PRINT,FORMAT='("Pb (mol)  : ",G0.8)',Pb  * N_A
PRINT,FORMAT='("SiO2 (mol): ",G0.8)',SiO2* N_A
PRINT,''
PRINT,FORMAT='("H2O (kg)  : ",G0.8)',H2Okg 
PRINT,FORMAT='("N2 (kg)   : ",G0.8)',N2kg  
PRINT,FORMAT='("Pb (kg)   : ",G0.8)',Pbkg  
PRINT,FORMAT='("SiO2 (kg) : ",G0.8)',SiO2kg

PRINT,''
PRINT,''
PRINT,''
PRINT,"PROBLEM 1.14"
PRINT,"************"
;Problem 1.14
O2   = O * 2

N2frac = 0.78D
O2frac = 0.21D
Arfrac = 0.01D

dryAir = N2*N2frac+O2*O2frac+Ar*Arfrac
dryAirkg = dryAir * N_A * uToKg

PRINT,FORMAT='("dryAir (u)  : ",G0.8)',dryAir 
PRINT,''
PRINT,FORMAT='("dryAir (mol) : ",G0.8)',dryAir * N_A
PRINT,''
PRINT,FORMAT='("dryAir (kg)  : ",G0.8)',dryAirkg 
