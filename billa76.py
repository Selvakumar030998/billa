#SSS
z12=int(input())
flag2=0
if(z12>2):
    for i in range(2,int(z12/2)+1):
        if z12%i==0:
            print("yes")
            flag2=1
            break
if flag2==0 or z12==2:
    print("no")
