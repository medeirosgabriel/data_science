setwd("C:/Users/Alba/Documents/R")
df <- read.csv("FipePrevAjustada.csv",header=TRUE,encoding="UTF-8")


# Tidyverse -> Package collections for Data Science

install.packages("tidyverse")

# Margrittr -> Operators that simplifies the scripts

install.packages("magritrr")
library(magrittr)

mean(df$Preço)

df$Preço %>% mean # %>% -> Operator pipe -> Chaining functions. Such artifice is from magrittr

# dplyr -> Consistent and fast for data manipulation

install.packages("dplyr")
library(dplyr)

View(df)

# Average car prices zero km per brand
brandMean <- df %>% filter(Ano_Modelo=="Zero KM") %>% group_by(Marca) %>% summarise(mean(Preço))

View(brandMean)

# tidyr <- Projected for data organization.
# Each variable in your column and each observation in your row.

install.packages('tidyr')

# stringr <- Simple, consistent and easy to use.
# Enables string processing

install.packages('stringr')