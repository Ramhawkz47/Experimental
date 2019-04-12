import os
n= input("file name:")
a= open(n,"r",encoding="utf-8")
x=""
for s in a:
    for c in s:
        z=ord(c)
        z=z-13

        if(z<0):
            z=z+256
            
        x=x+chr(z)

    print(x)
    with open("result2.txt", "w", encoding="utf-8") as f:
        f.write(x)
