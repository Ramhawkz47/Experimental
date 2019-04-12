print("existing command are:")
print("")
d={}
for s in open("test.txt", "r", encoding="utf-8"):
    print(s)
    for i in range(len(s)):
        if(s[i:i+3]=="---"):
            a=s[0:i-1]
            b=s[i+4:(len(s)-1)]
            d[a]=b

print(d)

print("enter input:(type 'bye' to exit)")
x=0
m= input("command:")
while(m.lower()!="bye"):
    if(d[m]!=""):
        y=input("existing command do you want to overwrite?(y/n):")
        if(y.lower()=="y"):
            print()
        else:
            x=1
            
    if(x==0):
        n= input("reply:")
        o=m+" --- "+n+"\n"
        print(o)
        with open("test.txt", "a", encoding="utf-8") as f:
            f.write(o)
    m= input("command:")
    x=0
print("done")
