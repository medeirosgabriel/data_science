setwd("C:/Users/Alba/Documents/R")

df <- read.csv("fipe_Jun2018.csv", header=TRUE,encoding='UTF-8')

View(df)
str(df)

# Delete Rows
df$X <- NULL
df$price_reference <- NULL

names(df)
names(df) <- c("Marca", "Carro", 'Ano_Modelo', "Combustível", "Preço")

summary(df$Ano_Modelo)

df$Ano_Modelo[df$Ano_Modelo==32000] <- "Zero KM" # Get the rows where Ano = 32000 and changing to Zero KM
df$Ano_Modelo <- as.factor(df$Ano_Modelo)

summary(df$Ano_Modelo)
str(df$Ano_Modelo)

summary(df$Preço)
df$Preço1 <- as.numeric(df$Preço) # It's wrong
summary(df$Preço1)
df$Preço1 <- NULL # Delete the row

df$Preço1 <- gsub("R\\$|\\.| ","",df$Preço) # Price is a character
df$Preço1 <- NULL # Delete the row

df$Preço <- gsub("R\\$|\\.| ","",df$Preço) # Delete the R$
summary(df$Preço)

df$Preço <- as.numeric(gsub("\\,",".",df$Preço)) # Remove the comma and put the stitch and turns into number
summary(df$Preço)

str(df)

write.table(df,file="FipeTransformada.csv",row.names=FALSE,sep=",",fileEncoding="UTF-8")