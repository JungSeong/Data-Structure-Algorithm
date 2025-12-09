import sys
INPUT = sys.stdin.readline
l = []

N = int(INPUT())
for i in range(N) :
    name, kor, eng, math = map(str, INPUT().split())
    l.append([name, int(kor), int(eng), int(math)])

l = sorted(l, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for row in l :
    print(row[0])