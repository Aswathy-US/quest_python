# Program to find sum of digits  of number

input_number = int(input('Enter a number to find sum of digits in it: '))

sum_of_even_digits = 0
temp_number = input_number
remainder_digit = 0

while temp_number != 0:
    remainder_digit = temp_number % 10
    temp_number = temp_number // 10
    sum_of_even_digits += remainder_digit

print(f'Sum of digits in {input_number} is {sum_of_even_digits}')
