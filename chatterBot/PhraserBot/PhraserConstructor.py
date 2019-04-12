print("existing command are:")
print("")
d={}
g=[]
h=[]
c={}
x=0
for s in open("test.txt", "r", encoding="utf-8"):
    print(s)
    for k in range(len(s)):
        if((s[k]==" ") and (s[k:k+4]==" ---")):
            c[s[0:k]]=s[k+5:len(s)-1]


print(c)
x=0
f=1
print("\n\n\n")
for s in c:
    S=c[s]
    for k in range(len(S)):
        if((S[k]==" ")):
            try:
                d[S[x:k]]=d[S[x:k]]+1
                x=k+1
                f=0
                print
            except:
                d[S[x:k]]=1
                x=k+1
                f=0
    if(f==1):
        d[S]=1

    else:
        f=1


print(d)
print("exit")
