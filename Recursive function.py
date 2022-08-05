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
def f1(x,y):
    #base case
    if y==0:
        return 1
    
    res= x * f1(x,y-1)
    return res
res=f1(2,3)
print(res)
