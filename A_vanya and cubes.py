n=int(input())

height=0
total=0
for i in range(1,n+1):
    total+= (i*(i+1)/2)
    if total<=n:
        height+=1
print(height)
        






