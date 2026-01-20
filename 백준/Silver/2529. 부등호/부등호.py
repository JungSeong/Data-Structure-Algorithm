import sys
input = sys.stdin.readline

k = int(input())
sign = tuple(input().split())
isVisited = [False] * 10
num = []

def BackTracking(cur, before, N) :
    if cur == len(sign) + 1 :
        num.append(N)
        return
    for i in range(10) :
        if not isVisited[i] :
            if cur == 0 :
                isVisited[i] = True
                BackTracking(cur+1, i, N + str(i))
                isVisited[i] = False
            else : 
                if sign[cur-1] == "<" and before < i :
                    isVisited[i] = True
                    BackTracking(cur+1, i, N + str(i))
                    isVisited[i] = False
                elif sign[cur-1] == ">" and before > i :
                    isVisited[i] = True
                    BackTracking(cur+1, i, N + str(i))
                    isVisited[i] = False

BackTracking(0, -1, "")
print(max(num) + "\n" + min(num))