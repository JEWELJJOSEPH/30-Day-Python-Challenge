# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

number = int(input("Enter a positive integer: "))
if number < 1:
    print("Please enter a positive integer.")
else:
    total_sum = 0
    for i in range(1, number + 1):
        total_sum += i
    print("The sum of all numbers from 1 to ", number , "is", total_sum)
