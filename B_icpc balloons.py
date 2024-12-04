t=int(input())

for i in range(t):
    seen=set()
    n=int(input())
    s=input()
    sum=0
    for c in s:
      
        if c not in seen:
            sum+=2
            seen.add(c)
        else:
            sum+=1
    print(sum)                


