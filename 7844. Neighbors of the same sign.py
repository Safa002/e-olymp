n=int(input())
a=list(map(int,input().split()))
i=0
while i<n-1:
    if (a[i]<0 and a[i+1]<0) or (a[i]>0 and a[i+1]>0):
        print(a[i],a[i+1])
    i+=1
