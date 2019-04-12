import os

a= open("result.txt","r",encoding="utf-8")
x=""
for s in a:
    for c in s:
        z=ord(c)
        z=256-z
        x=x+chr(z)

    print(x)
    with open("result2.txt", "w", encoding="utf-8") as f:
        f.write(x)
