n=int(input())
s=0
a=input()
for i in a:
    s=s^ord(i)
if s==0:
    print("Ok")
else:
    print(chr(s))
