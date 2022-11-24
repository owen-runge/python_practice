def primes(n):
    lst = []
    if n > 1:
        if checkPrime(n, 2):   #start at 2 and move upwards
            lst.append(n)
        lst = primes(n-1) + lst
        return lst
    lst.reverse()
    return lst

def checkPrime(num, divisor):
    if num < 2:
        return False
    if num == divisor:
        return True
    elif (num % divisor == 0):
        return False

    return checkPrime(num, divisor+1)

for i in range(1,12):
    print(primes(i))