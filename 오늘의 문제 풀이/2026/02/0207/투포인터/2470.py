# 서로 다른 용액 혼합해 특성값이 0에 가깝도록
import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left, right = 0, len(liquid)-1
result = abs(liquid[left] + liquid[right])
answer = [liquid[left], liquid[right]]

while left < right :
    if abs(liquid[left] + liquid[right]) <= result :
        answer = [liquid[left], liquid[right]]
        result = abs(liquid[left] + liquid[right])
    if liquid[left] + liquid[right] < 0 :
        left += 1
    elif liquid[left] + liquid[right] == 0 :
        break
    else :
        right -= 1

print(*answer)