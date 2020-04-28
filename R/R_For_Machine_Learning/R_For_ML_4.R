setwd("C:/Users/Alba/Documents/R")

df <- read.csv("FipeTransformada.csv",header=TRUE,encoding='UTF-8')

View(df)

levels(df$Carro)

# Column with Cilindradas

library(stringr)
# str_extract -> Extracts a pattern from a text

df$Cilindradas <- str_extract(df$Carro,'[0-9]\\.[0-9]')
str(df$Cilindradas)

df$Cilindradas <- as.factor(df$Cilindradas)
str(df$Cilindradas)
summary(df$Cilindradas)

unique(df$Carro[is.na(df$Cilindradas)])

# Does the same thing as unique:

library(dplyr)

df %>% filter(is.na(Cilindradas)) %>%
  select(Carro) %>%
  distinct(Carro)

# Select the automatic cars
aut <- subset(df, str_detect(df$Carro, " Aut\\."), "Carro")
aut <- unique(aut)
aut$Cambio <- "Aut"

View(aut)

# Select the manual cars
df <- left_join(df, aut)
df$Cambio[is.na(df$Cambio)] <- 'Med'
str(df$Cambio)

df$Cambio <- as.factor(df$Cambio)
str(df$Cambio)

# Car name column

library(tidyr)

df <- separate(df, "Carro", into="Nome", sep=" ",remove=FALSE)
summary(df$Nome)
df$Nome <- as.factor(df$Nome)
str(df$Nome)
str(df$Carro)

str(df)

df <- na.omit(df) # Delete rows with 'na'

write.table(df, file="FipePrev_2.csv",row.names=FALSE, sep=",",fileEncoding ='UTF-8')