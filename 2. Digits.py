n=int(input())
say=0
if n==0:
    print(1)
else:
    while(n>0):
        n=n//10
        say=say+1
    print(say)
