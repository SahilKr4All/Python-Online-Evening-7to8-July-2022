#sum of digits of no
result = 0
num = int(input("Enter No :"))
num_count = len(str(num))
for i in range(1,num_count+1):
    rem = num%10
    result += rem
    num =num//10

print(result)
    
    

