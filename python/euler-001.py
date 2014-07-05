# Find the sum of all the multiples of 3 or 5 below 1000

start = 0
end = 1000

three = []
five = []

for n in range (start, end):
    if (n%3 == 0):
        three.append(n)
    else:
        if (n%5 == 0):
            five.append(n)

print(sum(three) + sum(five))
