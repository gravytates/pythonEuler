from functools import reduce

# Sum of multiples of 3 and 5 up to 1000
# total = []
# for i in range(1000):
#     if i % 3 == 0:
#         total.append(i)
#     elif i % 5 == 0:
#         total.append(i)
#     else:
#         continue
#
# answer = reduce((lambda x, y: x + y), total)

# Sum of even fibonacci numbers up to 4 million

# fibList = []
# a,b = 0,1
# while b < 4000000:
#     if a % 2 == 0:
#         fibList.append(a)
#     if b % 2 == 0:
#         fibList.append(b)
#     a,b = b, a+b
#
# answer = reduce((lambda x,y: x + y), set(fibList))

# What is the largest prime factor of the number 600851475143 ?

def primes(m):
    primeNums = []
    for n in range(2,m):
        for x in range(2,n):
            if n%x == 0:
                break
        else:
            primeNums.append(n)
    return primeNums

def factorials(f):
    primeFactorials = []
    primeNums = primes(10000)
    for p in primeNums:
        if f % p == 0:
            primeFactorials.append(p)
    return primeFactorials

l=factorials(600851475143)
answer=l.pop()

print(answer)
