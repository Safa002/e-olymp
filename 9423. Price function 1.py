import math

x, k = map(float , input().split())
c = math.sqrt(math.fabs(x))
a = (c ** 4) + (k ** 3)
y = (math.log10(a) ** 3) + (math.cos(x) ** 5)

print(round(y, 2))
