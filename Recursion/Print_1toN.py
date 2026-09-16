# Print 1 to N Using Recursion

def print1toN(n, N):
    if n > N:
        return

    print(n)
    print1toN(n + 1, N)

N = int(input())
print1toN(1, N)