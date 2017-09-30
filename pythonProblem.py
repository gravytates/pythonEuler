# Sum of multiples of 3 and 5 up to 1000

from functools import reduce
total = []
for i in range(1000):
    if i % 3 == 0:
        total.append(i)
    elif i % 5 == 0:
        total.append(i)
    else:
        continue

grandTotal = reduce((lambda x, y: x + y), total)
print(grandTotal)
