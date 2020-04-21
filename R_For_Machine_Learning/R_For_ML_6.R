# Data Base

df <- data.frame(Person = seq(1:300),
                 Age = NA,
                 Weight = NA,
                 Height = NA,
                 Job = NA)

df$Age <- sample(20:60, 300, replace=TRUE)
df$Weight <- sample(45:120, 300, replace=TRUE)
df$Height <- sample(145:195, 300, replace=TRUE)
df$Job <- sample(0:1, 300, replace=TRUE)

df$Age[1:4] <- NA
df$Weight[20:102] <- NA
df$Height[108:250] <- NA

# Treatment missing data

View(df)

is.na(df)

any(is.na(df))

df_1 <- na.omit(df) # Delete the rows with NA

nrow(df)
nrow(df_1)

# Percentage of missing data

NAs <- round(colSums(is.na(df))*100/nrow(df), 2) # Rounds to two decimal places
NAs
NAs[NAs>0]

colSums(is.na(df)) # Sums the columns values, where values == NA
nrow(df)

NAs

df$Height <- NULL # Delete, because there is a lot of missing data

df$Weight[is.na(df$Weight)] <- mean(df$Weight, na.rm=TRUE) 
# na.rm = TRUE -> Considers 'NA' value to calculate the average

mean(df$Weight)
mean(df$Age) # NA, beacause by default na.rm == FALSE 

df_1 <- na.omit(df)

nrow(df)
nrow(df_1)

# Percentage of missing data
NAs <- round(colSums(is.na(df_1))*100/nrow(df_1),2)
NAs

any(is.na(df)) # Without data processing
any(is.na(df_1))