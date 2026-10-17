# Tuple Unpacking with zip : Using zip() function combines corresponding elements from multiple sequences
names = ("Krish", "Anant", "Sara")
scores = (85, 90, 95)

result = tuple(zip(names, scores))

print(result)

# Student information

students = ("Krish", "Amit", "Priya")
marks = (85, 90, 95)

result = zip(students, marks)

print(list(result))

# Product names and prices
products = ["Laptop", "Mouse", "Keyboard"]
prices = [60000, 800, 1500]

for product, price in zip(products, prices):
    print(f"{product}: ₹{price}")

# Adding two lists'element
a = [10, 20, 30]
b = [1, 2, 3]

for x, y in zip(a, b):
    print(x + y)


# Using zip to create dict
keys = ["name", "age", "course"]
values = ["Krish", 20, "AI"]

student = dict(zip(keys, values))

print(student)


# Unzipping using zip
print("===============")
pairs = (
    ("Krish", 85),
    ("Amit", 90),
    ("Priya", 95)
)

names, marks = zip(*pairs)

print(names)
print(marks)