import math
x1,y1,r1,x2,y2,r2=map(float,input().split())

if x1==x2 and y1==y2 and r1==r2:
    print(-1)
elif math.sqrt( (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) )== r1+r2 or math.sqrt( (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) )+r2 == r1 or math.sqrt( (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) )+r1==r2:
    print(1)
elif math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) )>r1+r2 :
    print(0)
elif math.sqrt( (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) )+r2<r1 or math.sqrt( (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) )+r1<r2:
    print(0)
else:
    print(2)
