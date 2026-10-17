# Unpacking database
database=[
  (101, "Krish", "AI", 90),
    (102, "Saniaa", "Python", 85),
    (103, "Dnyanda", "Data Science", 95)
]

for student_id, name, course, score in database:
    print(f"ID: {student_id}")
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Score: {score}")
    print("---")