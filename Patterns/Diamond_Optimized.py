n = 5

for i in range(1, 2 * n):
    if i <= n:
        stars = 2 * i - 1
    else:
        stars = 2 * (2 * n - i) - 1

    spaces = n - (stars + 1) // 2

    print(" " * spaces + "*" * stars)