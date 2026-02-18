import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for i in range(t) :
    n = int(input())
    phone_num = [input().rstrip() for _ in range(n)]
    phone_num.sort()
    isOK = True

    for i in range(1, len(phone_num)) :
        if phone_num[i].startswith(phone_num[i-1]) :
            isOK = False
            break

    if isOK :
        print("YES")
    else :
        print("NO")
    