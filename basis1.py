import math
i,j = map(int,(input().split()))
number = (i*j) 
root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print("yes")
else:
    print("no")
