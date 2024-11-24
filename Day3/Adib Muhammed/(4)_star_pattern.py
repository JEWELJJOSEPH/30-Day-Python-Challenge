print("Star Pattern Menu")
print("1. Pyramid Pattern")
print("2. Reverse Pyramid Pattern")
print("3. Right-Angle Triangle Pattern")
print("4. Diamond Pattern")
choice = int(input("Choose a pattern (1-4): "))
n = int(input("Enter the number of rows: "))

if choice == 1:
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

elif choice == 2:
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

elif choice == 3:
    for i in range(1, n + 1):
        print("*" * i)

elif choice == 4:
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

else:
    print("Invalid choice!")
