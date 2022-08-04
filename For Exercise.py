#Test

#1. take a number as an input ,  check whether the number is prime or not
#prime no - 1, itself
'''
x = int(input("Enter a Number :"))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime No")
'''

'''

#2. you have a list with some numbers...take a number as input and check whether it exists
#inside list or not
x = [1,2,3,4,4,5,56,90,-100,-1010]
y = int(input("Enter a Number :"))

if y in x:
    print("Found")
else:
    print("Not Found")
#3.'''
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
for i in range(1,6):
    print(" "*(5-i)+"* "*i)
'''
    *
   **
  ***
 ****
*****


1
22
333
4444
55555


1
12
123
1234
12345
'''
