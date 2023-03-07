library(reshape2)
cazy <- read.csv("../annotation_CAZymes/statistic_phylum_CAZy.csv",header = T,as.is = 1)
a <- melt(cazy)
write.csv(a,file="cazy_tableau.csv")
