#User Define -function
#Function Definition
'''
def f1():
    print("Function Called....")

#function Calling
f1()
'''

#parameterized function
'''
def add(x,y):
    print(x+y)


add(5,10)
'''
'''
def add(x,y):
    return x+y

res = add(50,90)
print(res)
'''

#calculator
def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def div(x,y):
    return x/y

def mul(x,y):
    return x*y

a = float(input("Enter No 1: "))
b = float(input("Enter No 2: "))

print('''
Press 1 for Addition
Press 2 for Subtraction
Press 3 for Division
Press 4 for Multiplication
''')

choice = int(input("Enter Choice : "))
'''
if choice==1:
    print(add(a,b))
elif choice ==2:
    print(minus(a,b))
elif choice == 3:
    print(div(a,b))
elif choice == 4:
    print(mul(a,b))
'''
dic = {1:add,2:minus,3:div,4:mul}
print(dic.get(choice)(a,b))

