setwd("C:/Users/Alba/Documents/R")

df <- read.csv("FipePrev_1.csv",header=TRUE, encoding='UTF-8')
View(df)

set.seed(100)

rows <- sample(1:length(df$Marca),length(df$Marca)*0.7)

training = df[rows,]

test = df[-rows,]

library(rpart)

model <- rpart(Preço ~.,data=training,control=rpart.control(cp=0))

test$Prevision <- predict(model, test)
View(test)

test$P <- abs(round(test$Prevision/test$Preço,4) - 1)
R_1 <- summary(test$P)
R_1 # Error rates

hist(df$Preço[df$Preço<quantile(df$Preço,0.90)],breaks=10,labels=T)

R_Final_1 <- summary(test$P[test$Preço>1000 & test$Preço<70000])
R_1
R_Final_1

dfReal <- read.csv('fipe_Jun2018.csv', header=TRUE,encoding='UTF-8')
View(dfReal)
View(df)