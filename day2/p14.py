def draw_triangle(lines):
    for i in range(1, lines + 1):
        print('*' * i)
lines = int(input("Enter the number of lines for the triangle: "))
draw_triangle(lines)
