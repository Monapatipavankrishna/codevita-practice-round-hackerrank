(ene,n)=map(int,input().split())
string=input()
try:
    z=[int(x) for x in string.split()]
except:
    print("Invalid input")
else:
    z.sort()
    for i in range(n):
        if ene>z[i]:
            ene=ene-(z[i]%2+z[i]/2)
        else:
            print("No");
            break;
    if i==n-1 and ene>0:
        print("yes")

