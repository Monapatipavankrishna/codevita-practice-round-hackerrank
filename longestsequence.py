n=int(input())
inp=input()
a=[int(x) for x in inp.split()]
count=0
i=0
b=[]
while i<n-2:   
    del b[:]
    if i!=0:
        i=i+1
    for x in range(i,n-1):
        if a[x]<=a[x+1]:
            i=i+1;
            b.append(a[x])
        else:
            break;
    if a[x]<=a[x+1] and i==n-1:
        b.append(a[x+1])
    else:
        b.append(a[x])
    c=len(b)
    if c>count:
        main=b[:]
        count=c;
#main=" ".join(str(x) for x in main)
#print(main)
for x in main:
    print(x,end=' ')
    
