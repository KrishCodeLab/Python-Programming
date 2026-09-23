# # Split a sentence into individual words using split().
# Count the number of words in a sentence using split() and len()

s=input("Enter String ")

# split(): The split() method is used to break a string into smaller parts and returns them as a list.
# If you don't give a separator, split() automatically uses whitespace.

print(s.split())
print(type(s.split()))
print(s.split())

# Split using a specific character : 
s = "apple,banana,mango"

print(s.split(","))
print(len(s.split(",")))


s = "2026-09-23"

print(s.split("-"))
print(len(s.split("-")))


# Store result in variable
s = "I love Python"

words = s.split()

print(words)
print(len(words))

print(words[0])
print(words[1])
print(words[2])

# split() with a limit
name="Krushna Govardhane From Nashik."
print(name.split(" ",2))
print(len(name.split(" ",2)))


