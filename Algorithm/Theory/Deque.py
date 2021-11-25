'''
    덱(deque, "deck"과 발음이 같음 ← double-ended queue)은 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료 구조의 한 형태이다.
'''

from collections import deque

deq = deque()

# Add element to the start
deq.appendleft(10)

# Add element to the end
deq.append(0)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()