input_number = int(input('Enter a number to count the number of odd digits in it: '))
count_of_odd_digits = 0
temp_number = abs(input_number)


while temp_number > 0:
    
    last_digit = temp_number % 10
    
    if last_digit % 2 != 0:
        count_of_odd_digits += 1
    
    temp_number //= 10


print(f'Number of odd digits in {input_number} is {count_of_odd_digits}')
