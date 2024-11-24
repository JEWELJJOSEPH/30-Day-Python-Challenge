choice = int(input("""Temperature Converter
1. Celsius to Fahrenheit
2. Celsius to Kelvin
3. Fahrenheit to Celsius
4. Fahrenheit to Kelvin
5. Kelvin to Celsius
6. Kelvin to Fahrenheit
Choose the conversion (1-6): """))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    print(celsius, "°C =", (celsius * 9/5) + 32, "°F")

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    print(celsius, "°C =", celsius + 273.15, "K")

elif choice == 3:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(fahrenheit, "°F =", (fahrenheit - 32) * 5/9, "°C")

elif choice == 4:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(fahrenheit, "°F =", (fahrenheit - 32) * 5/9 + 273.15, "K")

elif choice == 5:
    kelvin = float(input("Enter temperature in Kelvin: "))
    print(kelvin, "K =", kelvin - 273.15, "°C")

elif choice == 6:
    kelvin = float(input("Enter temperature in Kelvin: "))
    print(kelvin, "K =", (kelvin - 273.15) * 9/5 + 32, "°F")

else:
    print("Invalid choice!")
