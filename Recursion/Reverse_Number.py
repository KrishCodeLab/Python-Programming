def reverse_number(n, rev=0):
    # Base case
    if n == 0:
        return rev

    # Get last digit
    digit = n % 10

    # Add digit to reversed number
    rev = rev * 10 + digit

    # Recursive call
    return reverse_number(n // 10, rev)


num = 1234

result = reverse_number(num)

print("Reversed number:", result)