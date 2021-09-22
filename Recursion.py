def factorialWithRecursion(number):
    if number == 1:
        return number
    else:
        return number * factorialWithRecursion(number -1)

def factorialWithIteration(number):
    factorial = 1
    while (number != 1):
        factorial = factorial * number
        number-=1
    return factorial

print(factorialWithRecursion(5))
print(factorialWithIteration(5))
