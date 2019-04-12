import os

f= input("enter statement:")
x=""
for s in f:
    for c in s:
        z=ord(c)
        z=z+13

        if(z>256):
            z=z-256
            
        x=x+chr(z)

print("encrypted statement:"+x)

