# # Check whether a string contains only digits using isdigit().
# Check whether a string contains only alphabets using isalpha().
# Check whether a string contains only alphabets and numbers using isalnum().

s=input("Enter String here : ")

# isdigit():Returns True if all characters of string are digits
# isalpha():Returns True if all characters of string are alpha
# isalnum():Returns True if some are string contains alpha as well as digits 
# If there is only alpha still will return true vise versa for numbers

print("Checking Where all characters of string are digits ",s.isdigit())
print("Checking Where all characters of string  are alpha ",s.isalpha())
print("Checking Where some characters are alpha and some digits ",s.isalnum())
