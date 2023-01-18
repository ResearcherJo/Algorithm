'''
a = 97
'''

st = [-1 for i in range(26)]

s = list(input())

for i in s:
    st[ord(i)-97]=s.index(i)
    
for i in st:
    print(i,end=' ')
    
''' 좀 더 쉬운 코드
    string = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        print(string.find(i), end = ' ')
'''