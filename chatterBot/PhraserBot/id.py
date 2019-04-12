import random as r

a=[["he","it","she"],["him","they","her"]]
b=[["was","were"],["is","are"],["will","might"]]
c=["there","here"]
g={}
i=0

for x in a:
    for y in x:
        g[y]=i
    i=i+1

i=1

for x in b:
    for y in x:
        g[y]=i
    i=i+1

f=0
d={}

while(f<=10):
    m=r.randint(0,1)
    n=r.randint(0,2)
    o=r.randint(0,1)
    while((d[a[0][n]]%2!=0)and(d[a[n][m]]%2!=0)):
        m=r.randint(0,1)
        n=r.randint(0,2)
        o=r.randint(0,1)
    s=a[0][n]+" "+b[n][m]+" "+c[o]
    try:
        x=d[s]
        f=f+1
    except:
        d[s]=0


for s in d:
    print(s)
