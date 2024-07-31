#program to Print an equi lateral triangle of n lines

n = int(input('Enter the number of lines for the equilateral triangle: '))

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
