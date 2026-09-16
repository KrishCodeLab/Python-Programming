# What is recursion ?
# Recursion means a function calling itself 
# Every recursive function generally has:

# ✅ Base Case

# The condition that stops recursion.

# 🔄 Recursive Case

# The function calls itself with a smaller/simpler problem.

def print_numbers(n):
    if n == 6:       # Base case
        return

    print(n)
    print_numbers(n + 1)   # Recursive call


print_numbers(1)