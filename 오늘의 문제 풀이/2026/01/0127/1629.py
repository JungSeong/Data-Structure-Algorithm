import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def recursive(A, B) :
    if B == 0 :
        return 1 % C
    elif B % 2 == 0 :
        half = recursive(A, B//2)
        return half * half % C
    else :
        half = recursive(A, (B-1)//2)
        return half * half * A % C

print(recursive(A, B))