from sys import stdin

input = stdin.readline

#n!에 있는 2의 개수를 새는 방법
def two_count(n):
    count = 0
    while n!=0:
        n //=2
        count += n
    return count

#n!에 있는 5의 개수를 세는 방법
def five_count(n):
    count = 0
    while n!= 0:
        n//=5
        count += n
    return count

n, m = map(int, input().split())

# 빼는 이유는 조합을 구하는 식이 n!/r! * (n-r)!인데, 조합의 2의 개수는 n!의 2의 개수에다가 r!과 (n-r)!의 2의 개수를 뺀 것이다. 
# min을 쓰는 이유는 뒷자리가 0이려면 2 와 5의 쌍의 개수이기 때문에 둘 중 작은 것이 쌍의 개수이다.
print(min(two_count(n)-two_count(n-m)-two_count(m),five_count(n)-five_count(n-m) -five_count(m)))




'''
n, m = map(int,input().split())
n_p = r_p = nm_p = 1

for i in range(1,n+1):
    n_p *= i
    if i<=m:
        r_p *=i
    if i<=n-m:
        nm_p *=i

p = (n_p // (nm_p*r_p))

count=0

while p%10==0:
    if p%10==0:
        count+=1
        p//=10
    else:
        break
        
print(count)
'''
#빼는 이유는 나누니까 나누는건 내가 가진 2의 개수에서 걔가 가진 2의 개수를 뺀 것과 같으니까