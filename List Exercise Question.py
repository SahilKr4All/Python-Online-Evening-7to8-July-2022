#find the largest value from the List
x = [10,20,30,-100,-1000,500]
largest =x[0]
for value in x:
    if value>largest:
        largest = value

print(largest)
