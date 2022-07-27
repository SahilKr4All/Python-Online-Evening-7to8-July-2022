#sum of digits of no
result = 0
num = int(input("Enter No :"))
temp = num
num_count = len(str(num))
for i in range(1,num_count+1):
    rem = num%10
    result += rem**3
    num =num//10

    
if temp == result:
    print("Armstrong")
else:
    print("Not an Armstrong No")
    
    
    

