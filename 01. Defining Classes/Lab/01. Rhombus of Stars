def generate_row(index, n, symbol):
    indent = " " * (n - index)
    stars = symbol * index
    return indent + stars


def print_upper_rhombus_half(n, symbol):
    for i in range(1, n + 1):
        print(generate_row(i, n, symbol))


def print_lower_rhombus_half(n, symbol):
    for i in range(n - 1, 0, -1):
        print(generate_row(i, n, symbol))


n = int(input())
print_upper_rhombus_half(n, "* ")
print_lower_rhombus_half(n, "* ")
