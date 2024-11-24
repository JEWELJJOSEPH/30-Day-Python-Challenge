num = int(input("Enter a number: "))
digits = str(num)
num_digits = len(digits)
sum_of_powers = 0

for digit in digits:
    sum_of_powers += int(digit) ** num_digits

if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
