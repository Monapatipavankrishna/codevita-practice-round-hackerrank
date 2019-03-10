(n,m)=map(int,input().split())
if n==m:
    print("1");
    exit;
s=n
count=1
for i in range(n,0,-1):
    if s==m:
        break;
    if s<m:
        s=s+i-1
        count=count+1;   
        if s>m:
            s=s-i+1
            count=count-1;
if s!=m:
    print("-1")
else:
    print(count)
        
    
    
