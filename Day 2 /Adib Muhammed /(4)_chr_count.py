s = input("Enter the Sentence : ")
symbol_count = vowel_count = consonant_count = capital_count = small_count = 0
vowels = "aeiou"

for char in s:
    if char.isalpha():
        if char.lower() in vowels:
            vowel_count += 1
        elif char.lower() not in vowels:
            consonant_count += 1
        if char.isupper():
            capital_count += 1
        elif char.islower():
            small_count += 1
    else:
        symbol_count += 1

print("Total symbols:", symbol_count, "\nTotal vowels:", vowel_count, "\nTotal consonants:", consonant_count, "\nCapital letters:", capital_count, "\nSmall letters:", small_count)
