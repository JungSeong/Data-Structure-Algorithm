# 알고리즘 난이도가 d -> |d-Ti|가 작은 것이 좋음
# |d-Ti| 같음 -> 사전 순으로 먼저 오면 좋음

import sys
input = sys.stdin.readline

N = int(input())
algorithm = dict()
member = dict()

for i in range(N) :
    algo, d = input().split()
    d = int(d)
    algorithm[algo] = d

M = int(input())

for i in range(M) :
    name, T = input().split()
    T = int(T)
    member[name] = T

Q = int(input())
name = ""

for i in range(Q) :
    q = input().rstrip()
    if q != "nani ga suki?" :
        name = q.split()[0]
        print("hai!")
    else :
        T = member[name]
        distance = []
        for k, d in algorithm.items() :
            distance.append((abs(d-T), k))
        distance.sort()
        name1, name2 = distance[0][1], distance[1][1]
        print(f"{name2} yori mo {name1}")