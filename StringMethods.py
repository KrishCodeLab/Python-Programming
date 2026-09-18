# String Methods : Methods are in bulit function to perform specific operation on the string

name="krishna"

# upper() :- Converts all letters to uppercase.
print(f"Name in upper case {name.upper()}")

# upper() :- Converts all letters to lowercase.
print(f"Name in upper case {name.lower()}")

# title() :- Convert all words' first letter to Uppercase 
text = "krishna patil"
print(text.title())

# capitalize() :- Convert only first letter of the statement
text = "hello world"
print(text.capitalize())

# swapcase() :- Upper becomes lower and lower becomes upper.
text = "KrIsH"
print(text.swapcase())

# strip() :- Remove space from starting and ending of string 
text = "  Krish  "
print(text.strip())

# lstrip() :- Removes only starting space of string
print("  Hello".lstrip())

# rstrip() :- Removes only ending space of string
print("Hello   ".rstrip())
