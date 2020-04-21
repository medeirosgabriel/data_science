# <- Creates a variable
# = Function assignment. Some examples work others don't

a <- 10
b = 9
cat(a, b, '\n')

a -> b
print(b)

a <- 'Heitor'
b <- 'João'
# d <- a + b Error

d <- c(a, b) # c is a function that combines values into a vector or list.
print(d)

a <- c(10, 5, 15, 20)
print(a)

summary(a) # Statistical information about the variable

install.packages('stringr')
library('stringr')

name <- 'João'
sname <- 'Silva'

# str_c -> Função da biblioteca stringr

completeName <- str_c(name, sname)
print(completeName)
completeName <- str_c(name, ' ', sname)
print(completeName)
