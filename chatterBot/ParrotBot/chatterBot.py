import os

n= input("file name:")
g= open(n,"r")
d={}
for s in g:
    s=s.lower()
    for i in range(len(s)):
        if(s[i:i+3]=="---"):
            a=s[0:i-1]
            b=s[i+4:(len(s)-1)]
            d[a]=b

    print(d)
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(str(d))


print("")
n = input("type:")
while(n.lower() != "bye"):
    print("bot:"+d[n.lower()])
    print("")
    n = input("type:")

print("bye my friend!!!!!")
