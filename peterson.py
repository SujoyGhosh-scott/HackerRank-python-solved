n = int(input())


def factorial(n):
    if(n == 1):
        return n
    elif(n < 1):
        return ("NA")
    else:
        return n*factorial(n-1)


def peterson(n):
    num = n
    sum = 0
    while n > 0:
        digit = int(n % 10)
        sum += factorial(digit)
        n = int(n / 10)
    return (sum == num)


print("Yes" if peterson(n) else "No")
