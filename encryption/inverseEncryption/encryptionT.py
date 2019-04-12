import os

f= input("enter statement:")
x=""
for s in f:
    for c in s:
        z=ord(c)
        z=256-z            
        x=x+chr(z)

print("encrypted statement:"+x)

