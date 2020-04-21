# Data Filter

vowels <- c('a', 'e', 'i', 'o', 'u')

# Acessing the third element
vowels[3]

# Acessing all elements, except the third element
vowels[-3]

# Acessing third, fourth, fifth elements
vowels[3:5]

# Filter considering the length
length(vowels)
vowels[3:length(vowels)]
vowels[(length(vowels) - 2):length(vowels)]

a <- 3
b <- 5
vowels[3:5]

# Acessing through of conditions
vowels[vowels == 'e']
vowels[vowels != 'e']

a <- c(1, 2, 3, 4, 5)

a[a > 2]
a[a >= 2]

# Using DataFrames

setwd("C:/Users/Alba/Documents/R")
df <- read.csv("DataFrame.csv")

df[1]
df[1,] # First row with all columns

df[1:6]
df[-4] # All columns, except the fouth column

df[1,1]
df[1,1:6]
df[1,-4] # First line without fourth column

df[1:3, 1:6]
df[-1,-4]

# Changing the DataFrame
df <- df[c(-3,-4,-5,-6)] # Exclude the third, fourth, fifth as sixth columns
df

# Filtering the variables
df[1,1]
df$DIA_SEM[1]
df$AUTO[2:4]
df$UPS == 1 # True: the variable UPS == 1 | False: the variable UPS != 1
df[df$UPS == 1,] # Shows only where UPS == 1 

# Changing the DataFrame
df <- df[df$UPS == 1,]
df

# DataFrame x DataFrame_1
df_1 <- read.csv("DataFrame.csv")
View(df_1)
View(df)