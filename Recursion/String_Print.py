
def print_string(s, index):
    # Base case
    if index == len(s):
        return

    # Print current character
    print(s[index])

    # Recursive call
    print_string(s, index + 1)


print_string("KRISH", 0)
