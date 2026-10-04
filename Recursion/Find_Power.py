def power(base, exponent):

    # Base case
    if exponent == 0:
        return 1

    # Recursive case
    return base * power(base, exponent - 1)


print(power(2, 5))