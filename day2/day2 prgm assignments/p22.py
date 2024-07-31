#program to print the Pascals triangle of n lines

def print_pascals_triangle(n):
    
    triangle = [[1]]

    for i in range(1, n):
        row = [1] * (i + 1)  
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    for row in triangle:
        print(' '.join(map(str, row)))

try:
    n = int(input('Enter the number of lines for Pascal\'s Triangle: '))
    if n <= 0:
        print('Please enter a positive integer.')
    else:
        print_pascals_triangle(n)
except ValueError:
    print('Please enter a valid integer.')
