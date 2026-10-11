def string_length(s):
    # Base case
    if s == "":
        return 0

    # Recursive case
    return 1 + string_length(s[1:])


print(string_length("Krish"))