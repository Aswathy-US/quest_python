#program to print X shape made up of stars of n lines
def print_x_shape(n):
    if n <= 0:
        print('Please enter a positive integer.')
        return

    for i in range(n):
        for j in range(n):
            if j == i or j == (n - i - 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()

n = int(input('Enter the number of lines for the X shape: '))
print_x_shape(n)
