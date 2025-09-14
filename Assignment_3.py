#Task 1
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")

#Task 2
import math
n = int(input("Enter a number: "))
root = math.sqrt(n)
print(f"Square root: {root}")
log = math.log(n)
print(f"Logarithm: {log}")
sin = math.sin(n)
print(f"Sine: {sin}")