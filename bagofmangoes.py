n=int(input())
s=input()
su=0
a=[int(x) for x in s.split()]
for i in range(len(a)):
    su=su+a[i]
a.sort()
k=sum
for i in range(len(a)):
    if su%3==0:
        print(su);
        break;
    else:
        su1=0
        for j in range(i+1):
            su1=su1+a[j]
        if su1<a[i]:
            su=su-su1
        else:
            su=su-a[i]
        




            
    
