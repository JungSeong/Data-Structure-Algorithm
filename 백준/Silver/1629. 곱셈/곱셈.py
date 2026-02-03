import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def recursive(B) :
    if B == 0 :
        return 1 % C
    elif B % 2 != 0 :
        half = recursive((B-1)//2)
        return half*half*A%C
    else :
        half = recursive(B//2)
        return half*half%C

print(recursive(B))