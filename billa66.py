#S    
N1=int(input())
flag2=0
if N1>2:
    for i in range(3,int(N1/2)):
        if N1%i==0:
            flag2=1
            print("no")
            break
if flag2==0 or N1==2:
    print("yes")
