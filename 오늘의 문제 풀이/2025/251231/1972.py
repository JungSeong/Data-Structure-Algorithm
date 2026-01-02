import sys
input = sys.stdin.readline
strs = []

while True :
    st = input().strip()
    if st != "*" :
        strs.append(st)
    else :
        break

for st in strs :
    isPerfect = True
    for i in range(1, len(st)) :
        s = set()
        for j in range(len(st)-i) :
            s.add(st[j] + st[j+i])
        if len(s) != len(st)-i :
            isPerfect = False
            break
    if isPerfect :
        print(f"{st} is surprising.")
    else :
        print(f"{st} is NOT surprising.")