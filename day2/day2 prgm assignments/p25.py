#program to a hollow square of n lines
def print_hollow_square(n):
    if n <= 0:
        print('Please enter a positive integer.')
        return

    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

n = int(input('Enter the number of lines for the hollow square: '))
print_hollow_square(n)
