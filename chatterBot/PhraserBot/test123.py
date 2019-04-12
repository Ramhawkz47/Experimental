print("existing command are:")
print("")
for s in open("test.txt", "r", encoding="utf-8"):
    print(s)

print("enter input:(type 'bye' to exit)")

m= input("command:")
while(m.lower()!="bye"):
    n= input("reply:")
    o=m+" --- "+n+"\n"
    print(o)
    with open("test.txt", "a", encoding="utf-8") as f:
        f.write(o)
    m= input("command:")

print("done")
