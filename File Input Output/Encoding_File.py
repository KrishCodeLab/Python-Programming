# Encoding in File I/O :
# Computers store information as bytes. Encoding determines how text is converted into bytes and how bytes are converted back into text.

# Different encoding formats exist: UTF-8 , UTF-16 , ASCII , Latin-1
with open("student.txt","w",encoding="utf-8") as file:
  file.write("Name: Krish\n")
  file.write("नमस्ते")

with open("student.txt","r",encoding="utf-8") as file:
  print(file.read())