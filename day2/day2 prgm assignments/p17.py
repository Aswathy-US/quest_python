#program to find the sum of digits at even positions
a = int(input('Enter a number to find the sum of digits at even positions: '))


sum_of_even_placed_digits = 0
position = 1
temp_number = a


while temp_number != 0:
    remainder_digit = temp_number % 10  
    if position % 2 == 0:  
        sum_of_even_placed_digits += remainder_digit
    temp_number = temp_number // 10  
    position += 1  

print(f'Sum of digits at even positions in {a} is {sum_of_even_placed_digits}')
