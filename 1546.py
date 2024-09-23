

n = int(input())
a = input().split()


for i in range(n):
    a[i] = float(a[i])
    
a.sort(reverse = True)

max = a[0]

for i in range(n):
    a[i] = a[i]/max*100
    
ave = sum(a)/len(a)

print(ave)
    


     