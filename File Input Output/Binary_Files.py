# Working with binary files : 
# .jpg , .png , .mp3 , .mp4 , pdf files , executable files 

with open("Krishna1.jpg","rb") as source:
  data=source.read()
  print(data)

with open("Krishna_Govardhane_copy.txt","wb") as destination:
  destination.write(data)


# efficient way to handle large files
with open("Krishna1.jpg","rb") as source:
  with open("Krishna_Copy","wb") as destination:
    while True:
      # 1024 means 1KB
      chunk=source.read(1024)
    
      if not chunk:
        break

      destination.write(chunk)
