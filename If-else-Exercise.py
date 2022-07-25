x = int(input("Enter No1:"))
y = int(input("Enter No2:"))
z = int(input("Enter No3:"))

if x+y>z and x+y>z and x+y>z:
    if x==y and y==z :
        print("Equilateral Traingle")
    elif x==y or y==z or z==x:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Traingle cannot be formed....")
