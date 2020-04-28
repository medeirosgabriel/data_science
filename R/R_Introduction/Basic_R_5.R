# Data Frames -> Data base | csv, xlsx, etc.

# Defines Work Area
setwd("C:/Users/Alba/Documents/R")

# Import data base
df <- read.csv("DataFrame.csv")

# Analising The Data Frame
View(df)

# Data types
str(df)
summary(df)

# Selecting variables
df
df[1]
df$DIA_SEM

col_1 <- df[1]
col_2 <- df$DIA_SEM

class(df$DIA_SEM)
class(col_2)
class(col_1)

# Changing The DataFrame

# Deleting variable
df$ONIBUS <- NULL

# Changing The Data Variable inside DataFrame
df$UPS
summary(df$UPS)
df$UPS <- as.factor(df$UPS)
df$UPS
summary(df$UPS)

# Creating a new variable inside DataFrame
df$Nova <- 'a'
class(df$Nova)
df$Nova <- c(2, 5, 10)
df$Nova
# Error -> Number of rows is greater than the number of dataframe rows
# df$Nova <- c(2, 5, 10, NA, NA, NA, NA, NA, NA, NA)
df$Nova <- c(2, 5, 10, NA, NA, NA, NA, NA, NA)
df$Nova
df$Nova <- NULL
df$Nova
df$Nova <- NA
df$Nova
df$Nova[1:3] <- c(2, 5, 10)
class(df$Nova)