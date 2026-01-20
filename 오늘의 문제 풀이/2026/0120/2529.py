import sys
input = sys.stdin.readline

k = int(input())
st = ["0"] + list(input().split())

isUsed = [False]*10
ans = []

def BackTracking(cur, before, N) :
    if cur == len(st) :
        ans.append("".join(N))
        return
    for i in range(10) :
        if cur == 0 :
            isUsed[i] = True
            N.append(str(i))
            BackTracking(cur+1, i, N)
            isUsed[i] = False
            N.pop()
        else :
            if not isUsed[i] :
                if st[cur] == '<' and before < i :
                    isUsed[i] = True
                    N.append(str(i))
                    BackTracking(cur+1, i, N)
                    isUsed[i] = False
                    N.pop()
                elif st[cur] == '>' and before > i :
                    isUsed[i] = True
                    N.append(str(i))
                    BackTracking(cur+1, i, N)
                    isUsed[i] = False
                    N.pop()

BackTracking(0, -1, [])
print(max(ans))
print(min(ans))