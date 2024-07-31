#program to Count the number of Prime digits in a number
def count_prime_digits(number):

    prime_digits = '2357'
    count = 0

    for digit in str(number):
        if digit in prime_digits:
            count += 1

    return count

num = int(input('Enter a number: '))
print('The number of prime digits is:', count_prime_digits(num))
