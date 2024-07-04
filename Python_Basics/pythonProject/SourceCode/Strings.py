#WAP to count all letters, digits and special symbols for the given string

given_string = "N@#to26at^&i5ve"
letter_count = 0
digit_count = 0
symbol_count = 0

for char in given_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count +=1

print(f"Given String is {given_string}, Letter Count is {letter_count}, Digit count is {digit_count} and Symbol count is {symbol_count}")
