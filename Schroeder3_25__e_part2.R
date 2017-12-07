library(knitr)

## To log or not log temperature ...
do_png <- TRUE

## do_xLog <- FALSE
## log = ''
## if(do_xLog) {
    ## T <- c(c(1,5) %o% 10^(-3:5))            #In units of epsilon / k_B
##     log = 'xy'
## } else {
## T <- seq(0,1000,0.01)                #In units of epsilon / k_B
T <- seq(0,2,0.01)                #In units of epsilon / k_B
## T <- seq(0.975,0.985,0.00001)                #In units of epsilon / k_B
## }

## Heat capacity in units of N k_B
SolveMe <- 2*T - 1 / sinh(1/(2*T))
twoT <- 2*T
## cschtwo <- 1 / sinh(1/(2*T))
win <- 1 / (2*T)^2 * (1 / sinh(1/(2*T)))^2
## SolveMe <- 1 / sinh(1/(2*T))

## Give the chart file a name.
if(do_png) {
    ## png(file = "p3_25__part_e__solve_2T_eq_sinh_1_over_2T.png",pointsize=24,height=800,width=600)
    png(file = "p3_25__part_e.png",pointsize=24,height=800,width=600)
} else {
    x11()
}

this <- data.frame(T,SolveMe)

## Plot the bar chart. 
plot(T,win,type = "l", col = "black",
     xlab = 'T (in epsilon/k_B)',
     ylab = 'C (in units of N k_B)',
     main = "Einstein solid heat capacity vs. temperature",
     lwd = 2,log='')

## plot(T,twoT,type = "l", col = "black",
##      xlab = 'T',
##      ylab = '2T - 1 / sinh(1/2T)',
##      main = "Estimate stuff from Figure 1.14",
##      lwd = 2,log='xy')
## lines(T,cschtwo,col='blue')

## Was trying to solve something here, not sure what
## plot(T,SolveMe,type = "l", col = "black",
##      xlab = 'T',
##      ylab = '2T - 1 / sinh(1/2T)',
##      main = "Estimate stuff from Figure 1.14",
##      lwd = 2,log='xy')
## lines(T,twoT,col='green')
## lines(T,cschtwo,col='blue')



   ## main = "Entropy as function of temp",xlog=do_xLog,ylog=do_xLog)

## Save the file.
if(do_png) { dev.off() }
