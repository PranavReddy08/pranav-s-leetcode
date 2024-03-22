l=list(map(int,input().split()))
r=[]
for i in range(len(l)):
    c=0
    ll=len(l[i+1:])
    #print(ll)
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            c+=1
        else:
            break
    #print(c,ll)
    if c==ll:
        r.append(l[i])
print(r)
        
