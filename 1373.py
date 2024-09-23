from sys import stdin

input = stdin.readline

result = ''
s = input().strip()

while len(s)%3!=0:
    s = '0' + s

for i in range(0,len(s),3):
    result+=str(int(s[i])*4+int(s[i+1])*2+int(s[i+2])*1)

print(''.join(result))

import sys

n = sys.stdin.readline()
print(oct(int(n, 2))[2:])
