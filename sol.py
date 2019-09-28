n1=['aa','bb']
n2='aabbc'
lst=[]
for i in range(len(n1)):
    if n1[i] in n2:
        s=n2.find(n1[i])
        lst.append([s,s+len(n1[i])-1])
p = {(-1)}
for i in range(len(lst)-1):
    q=(set(range(lst[i][0],lst[i][1]+1)).union(set(range(lst[i+1][0],lst[i+1][1]+1))))
    p.update(q)

t1='<b>'
t2='</b>'
lp=list(p)
res=list(n2)
res.insert(lp[0],t1)
c=2

for i in range(1,len(lp)-1):
    if lp[i]+1==lp[i+1]:
        continue
    else:
        res.insert(lp[i]+c,t2)
        res.insert(lp[i+1]+c,t1)
        c+=2
        
    
    
    
    
res=''.join(res)
print('hi')
        
    
    
        
