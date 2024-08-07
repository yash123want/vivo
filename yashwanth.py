def fact(n):
    if n < 0 or int(n) != n:
        return "not defined"
    elif n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

f = int(input("Enter a number: "))
print("Factorial of the number is", fact(f))
