# Write a Python program to Check if a Year is a Leap Year or not

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year ,"is a leap year.")
else:
    print(year ,"is not a leap year.")
