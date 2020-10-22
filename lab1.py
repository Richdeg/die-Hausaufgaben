import math

def sum1(e1):
    sum = 0
    n = 0
    e = 1
    while e > e1:
        n += 1
        s = sum
        sum += 1 / (n * (n + 1))
        e = abs(s - sum)
    return sum, n

def sum2(e2):
    sum = 0
    n = 0
    e = 1
    while e > e2:
        n += 1
        s = sum
        sum += (-1) ** (n + 1) / math.factorial(n - 1)
        e = abs(s - sum)
    return sum, n


print(sum1(0.0000000000001))
print(sum2(0.0000000000000001))