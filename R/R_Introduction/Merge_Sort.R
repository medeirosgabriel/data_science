# MergeSort

mergeSort <- function(array, start, f) {
  
  if (start < f) {
    middle <- as.integer((start + f)/2)
    array <- mergeSort(array, start, middle)
    array <- mergeSort(array, middle + 1, f)
    array <- merge(array, start, middle, f)
  }
  
  return (array)
}

merge <- function(array, start, middle, f) {
  
  vec <- numeric(0)
  i <- 1
  p1 <- start
  p2 <- middle + 1
  
  while (p1 <= middle & p2 <= f) {
    if (array[p1] <= array[p2]) {
      vec[i] <- array[p1]
      p1 <- p1 + 1
    } else {
      vec[i] <- array[p2]
      p2 <- p2 + 1
    }
    i <- i + 1
  }
  
  while (p1 <= middle) {
    vec[i] <- array[p1]
    i <- i + 1
    p1 <- p1 + 1
  }
  
  while (p2 <= f) {
    vec[i] <- array[p2]
    i <- i + 1
    p2 <- p2 + 1
  }
  
  for (j in seq(length(vec))) {
    array[start + j - 1] <- vec[j]
  }
  
  return (array)
}

v <- c(-123,43,65,78,12,9,-45,-12,-46,-1, 17,678,790)

mergeSort(v, 1, length(v))

