# Vectors - Basic Data Structure

name_1 <- "Eduardo Abreu"
name_2 <- 'Amanda Lopes'
names <- c(name_1, name_2)

hours <- 220
salary <- 3450.89
l1 <- salary > hours

# Caracter vector

is.vector(names)
mode(names)

# Numeric Vector

is.vector(hours)
mode(hours)

# Logic Vector

is.vector(l1)
mode(l1)

# List - Vector with different types of values

a <- c(1, 2, 3, 4, 5)
b <- c(1, '2', 3, 4, 5) # Turn into a character vector
print(a)
print(b)

b <- as.numeric(b)
print(b)

is.list(a)
is.list(b)

is.vector(a) 
is.vector(b)

is.numeric(a)
is.numeric(b)
is.character(b)

b <- list(10, '2', 8)
is.list(b)
is.vector(b)
is.numeric(b)
mode(b)
str(b)

e <- list(c(10, 6, 51, 5), '2', 8)
str(e)
e[[1]][1] # e[[1]] -> Takes the first element
e[[1]][2]

# Matrix -> One data type

m <- matrix(1:9, nrow = 3) # nrow -> Number of columns | 1:9 -> Data
print(m)
mode(m)
class(m)

# m[row, column]
m[1, 3]
m[1, 3] <- 'a'

mode(m)
m
class(m)


