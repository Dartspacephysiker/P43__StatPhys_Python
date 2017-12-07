## To log or not log temperature ...
do_png <- TRUE

do_xLog <- FALSE
log = ''
if(do_xLog) {
    T <- c(1:9 %o% 10^(-3:3))            #In units of ( mu B ) / k_B 
    log = 'xy'
} else {
    T <- seq(0.1,10,0.1)                #In units of ( mu B ) / k_B
}

## Ubar <- N * tanh(1/T)                   #In units of U / (mu B)
Ubarbar <- tanh(1/T)                   #In units of U / (N mu B)

## Entropy as function of temperature, in units of N k_B
S <- log(2) + 0.5 * ( Ubarbar * log((1 - Ubarbar)/(1 + Ubarbar)) - log(1-Ubarbar^2) )


## Give the chart file a name.
if(do_png) {
    png(file = "p3_21__S_as_function_T.png",pointsize=24,height=800,width=600)
} else {
    x11()
}

## Plot the bar chart. 
plot(T,S,type = "o", col = "red", xlab = "T (in mu*B/k_B)", ylab = "S/k_B",
   main = "Entropy as function of temp",log=log)
   ## main = "Entropy as function of temp",xlog=do_xLog,ylog=do_xLog)

## Save the file.
if(do_png) { dev.off() }
