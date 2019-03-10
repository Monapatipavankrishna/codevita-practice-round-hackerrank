t=int(input())
output=list()
for j in range(t):
    negval=0
    power=1
    strength=0
    n=int(input())
    s=[int(x) for x in input().split()]
    for i in range(n):
        if negval>s[i]:
            negval=s[i]
        if strength+s[i]>=0:
            strength=strength+s[i]
        elif s[i]<0 and power!=0 and strength+s[i]<0:
            strength=strength+s[i]
            strength=strength-2*negval
            power=0
        else:
            strength=strength+s[i]
            output.append(i+1)
            break;
    if strength>=0:
        output.append("She did it!");
for i in range(len(output)):
    print(output[i])
        
        
    
    
