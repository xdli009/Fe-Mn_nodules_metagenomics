library(reshape2)
data <- read.table("ncyc_scyc_bin_table_all.txt", header = T, check.names = F, row.names = 1)
df <- melt(data)
write.csv(df,file="ncyc_scyc_bin_table_melt_all.csv")

