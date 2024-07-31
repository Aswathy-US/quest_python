#program to print the Fibo series of n terms with 1st 2 terms as 1 and 2.
def print_fibonacci_series(n):
    if n <= 0:
        print('Please enter a positive integer.')
        return
    elif n == 1:
        print('1')
        return
    elif n == 2:
        print('1 2')
        return

    a = 1
    b = 2
    series = [a, b]

    while len(series) < n:
        next_term = a + b
        series.append(next_term)
        a = b
        a = next_term

    print(' '.join(map(str, series)))

n = int(input('Enter the number of terms for the Fibonacci series: '))
print_fibonacci_series(n)
