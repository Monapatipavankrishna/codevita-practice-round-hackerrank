n=int(input())
a=[int(x) for x in input().split()]
m=int(input())
val=0
k=0
s=0;i=0;
output=[]
for j in range(m):
    b=int(input())
    s=0
    for i in range(n):
        if b>s:
            s=s+a[i]
        else:
            output.append(i)
            break;
        if b<=s and i==n-1:
            output.append(i+1)
    if b>s:
        output.append(-1)

for i in output:
    print(i)
    
            
        
