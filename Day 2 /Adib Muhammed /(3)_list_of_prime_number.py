n = int(input("Enter the number : "))
primes = []

for num in range(2, n + 1):
    is_prime = True
    for p in primes:
        if num % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

for i in range(0, n + 1, 10):
    row = []
    for p in primes:
        if i < p <= i + 10:
            row.append(p)
    
    for p in row:
        print(p, end=" ")
    print()  
