
try:
    x = int(input("Enter No1:"))
    y = int(input("Enter No2:"))
    
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    x = [1,2,3,4,5]
    #print(x[1000])

except BaseException as be:
    print(be)

finally:
    print("Finished....")
