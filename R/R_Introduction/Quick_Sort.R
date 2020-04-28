# Sorting Algorithm - QuickSort

array <- c(-12, 32, -54, -67, 213, 545, 1, -5, 656)

quickSort <- function(array, pleft, pright) {
  if (pleft < pright) {
    result <- partition(array, pleft, pright)
    print(result)
    array <- result[1:length(result) - 1]
    pivotPosition <- result[length(result)]
    array <- quickSort(array, pleft, pivotPosition - 1)
    array <- quickSort(array, pivotPosition + 1, pright)
  }
  return(array)
}

partition <- function (array, pleft, pright) {
  pivot = array[pleft]
  p1 = pleft
  p2 = pright
  while (p1 <= p2) {
    if (array[p1] <= pivot) {
      p1 <- p1 + 1
    }else if (array[p2] > pivot ) {
      p2 <- p2 - 1
    }else{
      temp <- array[p1]
      array[p1] <- array[p2]
      array[p2] <- temp
    }
  }
  array[pleft] <- array[p2]
  array[p2] <- pivot
  return (c(array, p2))
}

array <- quickSort(array, 1, length(array))

print(array)

