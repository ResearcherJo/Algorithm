

N = int(input())

L = list()

for i in range(N):
    age, name = input().split()
    age = int(age)
    
    L.append([age,name])
    
L.sort(key = lambda x:x[0])

for i in L:
    print(i[0],i[1])