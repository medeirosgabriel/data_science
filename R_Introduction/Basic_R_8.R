# Creating functions

a <- c(423, 464, 69, 519, 123, 258)

x <- 0
for (i in a) {
  x <- x + 1
}
print(x)

b <- c(51, 36, 123, 98, 23, 37, 63, 3)

x <- 0
for (i in b) {
  x <- x + 1
}
print(x)

soma <- function(y) {
  x <- 0
  for (i in y) {
    x <- x + i
  }
  print(x)
}

soma(a)
soma(b)

soma_2 <- function(y, z) {
  x <- 0
  c <- 0
  for (i in y) {
    c <- c + 1
    x <- z[c] + i
    print(x)
  }
}

soma_2(a,b)
soma_2(b,a)

sum(a)
sum(b)
