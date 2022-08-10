#recursive function
'''
def f1(x):
    #base case
    if x>5:
        return
    print(x)
    f1(x+1)
    print(x)
f1(1)
'''
'''
def f1(x,y):
    #base case
    if y==0:
        return 1
    
    res= x * f1(x,y-1)
    return res
res=f1(2,3)
print(res)
'''
'''
result = 0
def f1(x):

    if x==10:
        return 10
    return x+ f1(x+1)

res=f1(1)
print(res)
'''
'''
*
**
***
****
*****

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
'''
'''
1
22
333
4444
55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

'''

'''
1
12
123
1234
12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
'''
1
23
456
78910
'''
'''
x=1
for i in range(1,5):
    for j in range(1,i+1):
        print(x,end="")
        x+=1
    print()
'''
'''

*****
*   *
*   *
*   *
*   *
*   *
*****


for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==1 or i==5 or j==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()


'''
'''

*   *
*   *
*   *
*****
*   *
*   *
*   *


*    *
* *  *
*  * *
*   **
*    *

'''


















