N = int(input("Enter N: "))
total = 0
while N > 0:
    total += N % 10
    N //= 10
print(total)
