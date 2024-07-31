# program to find the second smallest digit in it
input_number = int(input('Enter a number to find the second smallest digit in it: '))

number = input_number
digits = []
while number > 0:
    digit = number % 10
    if digit not in digits:
        digits.append(digit)  
    number //= 10  

if len(digits) < 2:
    print('The number does not have a second smallest digit.')
else:
    digits.sort()  
    print(f'The second smallest digit in {input_number} is {digits[1]}')
