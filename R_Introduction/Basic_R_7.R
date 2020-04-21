# Condition an action

# if TRUE
if (5 == 5) 6 + 6

# if TRUE else
if (5 == 5) 6 + 6 else "Unmet condition"

# Best practices

if (5 == 5){
  6 + 6
}else {
  "Condição não atendida"
}

# Example

ages <- c(25, 30)
names <- c("João", "Caina")
df = data.frame(names, ages)


if (df$ages[df$names == "João"] > df$ages[df$names == "Caina"]) {
  print("Mais velho: João")
} else {
  print("Mais velho: Caina")
}

ages <- c(25, 30, 24, 29, 31, 12)
names <- c("João", "Caina", "Maria", "Leo", "Lia", "Enzo")
df <- data.frame(names, ages)
View(df)

for (i in ages) {
  print(i)
}

v <- 0

for (i in df$ages) {
  if (i > v) {v <- i}
}
df$names[df$ages == v]

# While it's TRUE do that...

x <- 0
while(x < 10) {
  print(x)
  x <- x + 1
}

x <- 0
y <- 0
counter <- 0
ages100 <- 0

while (y < 100) {
  counter <- counter + 1
  ages100[counter] <- ages[counter]
  x <- x + ages[counter]
  y <- x + ages[counter + 1]
}

ages
ages100
sum(ages100)

