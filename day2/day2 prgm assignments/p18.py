# program to find the biggest digit in a number
input_number = int(input('Enter a number to find the biggest digit in it: '))

max_digit = 0
temp_number = abs(input_number)  

while temp_number != 0:
    remainder_digit = temp_number % 10  
    if remainder_digit > max_digit:  
        max_digit = remainder_digit
    temp_number = temp_number // 10  

print(f'The biggest digit in {input_number} is {max_digit}')
