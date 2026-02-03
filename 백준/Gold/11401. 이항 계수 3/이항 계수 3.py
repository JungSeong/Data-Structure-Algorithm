import sys
input = sys.stdin.readline

p = 1000000007

N, K = map(int, input().split())
factorial = [1]*(N+1)

for i in range(2, N+1) :
    factorial[i] = factorial[i-1] * i % p

def pow_num(num, mul) :
    if mul == 0 :
        return 1%p
    elif mul % 2 == 1 :
        half = pow_num(num, (mul-1)//2)
        return half*half*num%p
    else :
        half = pow_num(num, mul//2)
        return half*half%p

print(factorial[N]*pow_num(factorial[K]*factorial[N-K], p-2) % p)