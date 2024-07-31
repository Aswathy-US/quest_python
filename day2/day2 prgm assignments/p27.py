#Program to print a hollow square of n line with the diagonals

def print_hollow_square_with_diagonals(n):
    if n <= 0:
        print('Please enter a positive integer.')
        return

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or j == (n - i - 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()

n = int(input('Enter the number of lines for the hollow square with diagonals: '))
print_hollow_square_with_diagonals(n)
