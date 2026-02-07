# N <= 10^6

import sys
input = sys.stdin.readline

N = int(input())
num = list()

for i in range(10) :
    st = ""
    added = []
    st += str(i)
    for elem in num :
        st += elem
        added.append(st)
        st = st[:1]
    num.append(st)
    for elem in added :
        num.append(elem)

num = list(map(lambda x : int(x), num))
num.sort()

if N < len(num) :
    print(num[N])
else :
    print(-1)