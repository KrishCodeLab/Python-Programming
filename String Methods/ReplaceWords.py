# # Replace all spaces with - using replace().
# Replace "Java" with "Python" using replace().

n=input("Enter String ")


# replace():The replace() method is used to replace one part of a string with another.It returns a new string. The original string is not changed
# string.replace(old, new)


word_to_replace=input("Enter word to replace the old word ")

print(n.replace("Hello",word_to_replace))


s = "banana"

print(s.replace("a", "o"))

s = "Hello World Python"

print(s.replace(" ", "-->"))

# string.replace(old, new, count)

s = "banana"

print(s.replace("a", "o", 2))
