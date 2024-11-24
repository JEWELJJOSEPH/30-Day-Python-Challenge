print("Alphabet Pattern Menu")
print("1. Pyramid Alphabet Pattern")
print("2. Reverse Pyramid Alphabet Pattern")
print("3. Right-Angle Triangle Alphabet Pattern")
print("4. Diamond Alphabet Pattern")
choice = int(input("Choose a pattern (1-4): "))
n = int(input("Enter the number of rows: "))

if choice == 1:
    for i in range(n):
        spaces = " " * (n - i - 1)
        letters = ""
        for j in range(i + 1):
            if j != 0:
                letters += " "
            letters += chr(65 + j)
        print(spaces + letters)

elif choice == 2:
    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        letters = ""
        for j in range(i):
            if j != 0:
                letters += " "
            letters += chr(65 + j)
        print(spaces + letters)

elif choice == 3:
    for i in range(1, n + 1):
        letters = ""
        for j in range(i):
            if j != 0:
                letters += " "
            letters += chr(65 + j)
        print(letters)

elif choice == 4:
    for i in range(n):
        spaces = " " * (n - i - 1)
        letters = ""
        for j in range(i + 1):
            if j != 0:
                letters += " "
            letters += chr(65 + j)
        print(spaces + letters)

    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        letters = ""
        for j in range(i + 1):
            if j != 0:
                letters += " "
            letters += chr(65 + j)
        print(spaces + letters)

else:
    print("Invalid choice!")
