

x, y, w, h = map(int, input().split())

mn =1001
if abs(w-x)<mn:
    mn=abs(w-x)
if abs(h-y)<mn:
    mn=abs(h-y)
if abs(x-0)<mn:
    mn=abs(x-0)
if abs(y-0)<mn:
    mn=abs(y-0)
    
print(mn)