library(knitr)

## To log or not log temperature ...
do_png <- TRUE

## do_xLog <- FALSE
## log = ''
## if(do_xLog) {
##     T <- c(1:9 %o% 10^(-3:3))            #In units of epsilon / k_B
##     log = 'xy'
## } else {
    T <- seq(-2,2,0.05)                #In units of epsilon / k_B
## }

## Heat capacity in units of N k_B
Cv <- 1 / (4 * T^2) / (sinh(1/(2*T)))^2

## Give the chart file a name.
if(do_png) {
    png(file = "p3_25__Einstein_solid__C_v_as_func_of_t.png",pointsize=24,height=800,width=600)
} else {
    x11()
}

## Plot the bar chart. 
plot(T,Cv,type = "l", col = "red",
     xlab = expression(paste('T (in ', epsilon)*'/ k'['B']*')'),
     ylab = expression(paste('C'['v']*'/ N k'['B'])),
     main = "Heat Capacity of an Einstein Solid",
     lwd = 2)
   ## main = "Entropy as function of temp",xlog=do_xLog,ylog=do_xLog)

## Save the file.
if(do_png) { dev.off() }
