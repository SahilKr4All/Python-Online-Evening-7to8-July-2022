#access modes - read(r)/write(w)/append(a)
data = "Hello Everyone ,,,,How are you ?"
with open("abc.txt","w") as file:
    file.write(data)
    
