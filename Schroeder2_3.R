## Create the data for the chart.
nCoins <- 50
nHeads <- seq_len(nCoins)
nPoss <- 2^nCoins
prob <- choose(nCoins,nHeads)/nPoss


## Give the chart file a name.
png(file = "p2_2__probability_n_heads.png",pointsize=24,height=800,width=600)
## x11()

## Plot the bar chart. 
plot(nHeads,prob,type = "o", col = "red", xlab = "# Heads", ylab = "Probability",
   main = "Probability of obtaining heads")

## Save the file.
dev.off()
