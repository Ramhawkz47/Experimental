import os
n= input("file name:")
a= open(n,"r")
x=""
for s in a:
    for c in s:
        z=ord(c)
        z=z+13

        if(z>256):
            z=z-256
            
        x=x+chr(z)

    print(x)
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(x)
#f = open("result.txt","w+")
#f.write(x)
#f.close()
x=""

