# Numeric Storage

salary <- 3450.89
hours <- 220

sh <- salary/hours
print(sh)

shi <- as.integer(salary/hours) # This function takes the entire part of the number
print(shi * 5)

shr <- round(salary/hours) # This function round the number
print(shr)

number_1 <- salary + hours
print(number_1)

number_2 <- c(salary, hours)
print(number_2)

# Caracters storage

name_1 <- "Eduardo Abreu"

name_2 <- 'Amanda Lopes'

age <- 'Eduardo tem 25 anos'
print(age)

age <- '25'
print(age)

# names <- name_1 + name_2 -> ERROR
print(names)

names <- c(name_1, name_2)
print(names)

print(names[1])
print(names[2])

# Factors Storage

workload <- c(220,220,150,100,100)
summary(workload)

workload <- as.factor(workload) # Changes the execution of the summary
summary(workload) # Categorizes values

workload <- as.factor(c(220,220,150,100,100))
summary(workload)
mode(workload)
class(workload)

# Logic Storage

l1 <- salary > hours
print(l1)

l2 <- salary < hours
print(l2)

logic <- TRUE
print(logic)

logic <- 'True' # Caracter
print(logic)

logic <- c(1, TRUE, 3)
print(logic)

