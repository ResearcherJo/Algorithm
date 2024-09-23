'''
수학에서 에라토스테네스의 체는 소수를 찾는 방법이다. 고대 그리스 수학자 에라토스테네스가 발견하였다.
한편, 에라토스테네스의 체를 이용해 1~n까지의 소수를 알고 싶다면, n까지 모든 수의 배수를 다 나눠 볼 필요는 없다. 만약 n보다 작은 어떤 수 m이 m=ab라면 a와 b중 적어도 하나는 n의 제곱근이하이다. 
즉 n보다 작은 합성수 m은 n의 제곱근 보다 작은 수의 배수만 체크해도 전부 지워진다는 의미이므로, n의 제곱근 이하의 수의 배수만 지우면 된다.
'''

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [False,False] + [True] * (n-1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]