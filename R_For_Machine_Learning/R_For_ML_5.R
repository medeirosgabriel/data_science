setwd("C:/Users/Alba/Documents/R")

df <- read.csv("FipePrev.csv",header=TRUE,encoding='UTF-8')

View(df)

# Training Data - 70%
training <- df[1:7,]

# Data Test - 30%
test <- df[8:10,]

View(training)
View(test)

length(df$Marca)*0.7
length(df$Marca)

training = df[1:13698,]
test = df[13699:19569,]

View(training)
View(test)

length(training$Marca) + length(test$Marca)

# Random separation - Best choice
# sample(x:y,z)
# x:y -> Choice Interval  
# z -> Number of numbers

sample(1:6,1)
sample(1:19569,13698)

set.seed(100) # Random number

rows <- sample(1:length(df$Marca),length(df$Marca)*0.7)

training = df[rows,]

test = df[-rows,]

length(training$Marca) + length(test$Marca)

# Create a model

library(rpart) # Decision Tree Algorithm

model <- rpart(Preço ~., # We wanna predict the price considering all variables
               data=training, # Training Data
               control=rpart.control(cp=0)) # r.part is a function that control details algorithm.

# Make predictions

test$Previsão <- predict(model, test)

# Analyze results

test$P <- round(test$Previsão/test$Preço,2) # Error Percent
test$P <- test$P - 1
test$P <- abs(test$P)
R_1 <- summary(test$P)
R_1

# Analyze the price distribution

summary(df$Preço)

quantile(df$Preço,0.90) # Returns the value that is in the position regarding the percentage

hist(df$Preço[df$Preço<quantile(df$Preço,0.90)], breaks=10,labels=T)

R_Final_1 <- summary(test$P[test$Preço>10000 & test$Preço<70000])
R_1
R_Final_1

### Model 2 ###

# Without variable car

df$Carro <- NULL

training = df[rows,]
test = df[-rows,]

model <- rpart(Preço ~., # We wanna predict the price considering all variables
               data=training, # Training Data
               control=rpart.control(cp=0)) # r.part is a function that control details algorithm.

test$Previsão <- predict(model, test)
test$P <- round(test$Previsão/test$Preço,2)
test$P <- test$P - 1
test$P <- abs(test$P)
R_2 <- summary(test$P)
R_1
R_2

R_Final_2 <- summary(test$P[test$Preço>10000 & test$Preço<70000])
R_Final_1
R_Final_2

write.table(df,file="FilePrevAjustadaFinal.csv", row.names=FALSE, sep=",", fileEncoding="UTF-8")

