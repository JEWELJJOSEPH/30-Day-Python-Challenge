numbers = [2, 5, 22, 67, 40, 11, 43, 66, 34, 7]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
