## N <- 1e23
## mu <- this
## k_B <- 1.381e-23                        #J/K

## To log or not log temperature ...
do_png <- TRUE

do_xLog <- FALSE
if(do_xLog) {
    T <- c(1:9 %o% 10^(3:7))            #In units of ( mu B ) / k_B 
} else {
    T <- seq(0.1,10,0.1)                #In units of ( mu B ) / k_B

}

## Ubar <- N * tanh(1/T)                   #In units of U / (mu B)
Ubarbar <- tanh(1/T)                   #In units of U / (N mu B)

## Entropy as function of temperature
## S <- N*log(N) + 0.5 * log((N^2 - Ubar^2)) - 0.5 * log((N - Ubar)/(N + Ubar))
## S <- N*log(N) + 0.5 * log(N^2 * (1 - (Ubar/N)^2 ) ) - 0.5 * log((1 - Ubar/N)/(1 + Ubar/N))
## S <- N*log(N) + 0.5 * log(N^2) +0.5 * log(1 - (Ubar/N)^2 ) ) - 0.5 * log((1 - Ubar/N)/(1 + Ubar/N))
## S <- N*log(N) + log(N) + 0.5 * log(1 - (Ubar/N)^2 ) ) - 0.5 * log((1 - Ubar/N)/(1 + Ubar/N))
## S <- log(N) * ( N + 1 ) + 0.5 * log(1 - (Ubar/N)^2 ) ) - 0.5 * log((1 - Ubar/N)/(1 + Ubar/N))
## S <- log(N) * ( N + 1 ) + 0.5 * log(1 - (Ubar/N)^2 ) ) + 0.5 * log((1 + Ubar/N)/(1 - Ubar/N))
## S <- log(N) * ( N + 1 ) + log(1 + Ubar/N) 
S <- log(1 + Ubarbar) 


## Give the chart file a name.
if(do_png) {
    png(file = "p3_21__S_as_function_T.png",pointsize=24,height=800,width=600)
} else {
    x11()
}

## Plot the bar chart. 
plot(T,S,type = "o", col = "red", xlab = "T (in mu*B/k_B)", ylab = "S/k_B",
   main = "Entropy as function of temp",xlog=do_xLog)

## Save the file.
if(do_png) { dev.off() }
