start <- 0
end <- 1000-1

three <- seq(start, end, 3)
five <- seq(start, end, 5)

elements <- sort(union(three, five))
result <- sum(elements)

print(result)
