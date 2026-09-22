def power(p, n):
    if n == 0:
        return 1
    return p * power(p, n - 1)


p = float(input("Enter principal growth factor: "))
n = int(input("Enter number of years: "))

result = power(p, n)

print("P^n =", result)