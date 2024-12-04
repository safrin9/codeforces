t=int(input())

o="Timur"
for i in range(t):
    n= int(input())
    s=input()
    s=sorted(s)
    r=[]
   
    if len(s)>5:
        print("NO")
    
    else:
        r=list(o)
        if s==r:
            print("yes")
        else:
            print("no")