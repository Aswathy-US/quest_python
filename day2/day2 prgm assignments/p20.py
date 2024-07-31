#program to Check if a number is Prime number
num = int(input('Enter a number to check if it is prime: '))

if num <= 1:
    print(f'{num} is not a prime number.')
else:
    i = 2
    limit = num // 2  
    while i <= limit:
        if num % i == 0:
            print(f'{num} is not a prime number.')
            break
        i += 1
    else:
        print(f'{num} is a prime number.')
