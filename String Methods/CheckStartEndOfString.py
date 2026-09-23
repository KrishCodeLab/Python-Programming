# Check whether a string starts with "Hello" using startswith().
# Check whether a string ends with ".com" using endswith().
s=input("Enter string : ")
# startswith():Returns true if the starting of string is equal to parameter passsed to method else False
# endswith():Return true if the ending of string is equal to parameter that is passed to method else False
check=input("Enter to check start of string")

print(s.startswith(check))
print(s.startswith("Hello"))

print(s.endswith(" "))
print(s.endswith("Bye"))


