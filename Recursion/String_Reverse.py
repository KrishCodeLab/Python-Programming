
def reverse_string(s, index):
    # Base case
    if index == len(s):
        return

    # Recursive call first
    reverse_string(s, index + 1)

    # Print after the recursive call
    print(s[index], end="")


reverse_string("PYTHON", 0)
print()
