'''
def Rupee(x):
    return x/100

l1 = [100.2,345.4,3453454,3432,0.500,10000]
'''
'''
for item in l1:
    print(Rupee(item))
'''
'''
res=map(Rupee,l1)
for i in res:
    print(i)
'''
'''
#lambda function / single line function
f1 = lambda x : True if x%2==0 else False

l = [i for i in range(1,21)]
'''
'''
for i in l:
    value = f1(i)
    if value == "Even":
        print(i)
'''
'''
data=list(filter(f1,l))
print(data)
'''
'''
def f1(roll,name,*args):
    print(f"Roll No = {roll}")
    print(f"Name =  {name}")
    print(f"{args}")

f1(101,"Rohit",9876543210,"rohit123@gmail.com")
'''
#kwargs - keyworded-key-value-Dictionary arguments
def f1(roll,name,**kwargs):
    print(f"Roll No = {roll}")
    print(f"Name =  {name}")
    print(f"{kwargs}")

f1(101,"Rohit",phoneNo=9876543210,email_id="rohit123@gmail.com")
















