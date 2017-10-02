from functools import reduce
import math

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

# def primes(m):
#     primeNums = []
#     for n in range(2,m):
#         for x in range(2,n):
#             if n%x == 0:
#                 break
#         else:
#             primeNums.append(n)
#     return primeNums

# def factorials(f):
#     primeFactorials = []
#     primeNums = primes(10000)
#     for p in primeNums:
#         if f % p == 0:
#             primeFactorials.append(p)
#     return primeFactorials
#
# l=factorials(600851475143)
# answer=l.pop()

# Find the 10001st prime number

# m = 3
# primeNums = []
#
# while len(primeNums) < 10000:
#     for n in range(2,m):
#         for x in range(2,n):
#             if n%x == 0:
#                 m+=1
#                 break
#         else:
#             m+=1
#             if n not in primeNums:
#                 primeNums.append(n)
#
# print([primeNums[10000], len(primeNums), primeNums])

# Find the largest product of 13 adjacent numbers in a given 1000 digit number

# bigNum = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
#
# bigArray = [int(d) for d in str(bigNum)]
# a = 0
# b = 13
# productArray = []
# while b <= len(bigArray):
#     product = 1
#     subArray = bigArray[a:b]
#     a += 1
#     b += 1
#     for i in subArray:
#         product *= i
#     productArray.append(product)
#
# for n in range(len(productArray)-1,0,-1):
#     for i in range(n):
#         if productArray[i] > productArray[i+1]:
#             productArray[i], productArray[i+1] = productArray[i+1], productArray[i]
#
# print(productArray)

# Difference between Square of Sums and Sum of squares from 1 to 100
# squares = 0
# sums = 0
# for i in range(1,101):
#     squares += i ** 2
#     sums += i
#
# print((sums ** 2) - squares)


# Sum prime numbers up to 2000000
primeNums = [2]
for n in range(3,2000000,2):
    o = int(math.sqrt(n))
    for x in range(3,(o+1),2):
        if n%x == 0:
            break
    else:
        primeNums.append(n)

answer = reduce((lambda x, y: x + y), primeNums)

print(answer)
