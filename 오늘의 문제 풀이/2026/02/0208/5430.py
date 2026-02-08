import sys, re
from collections import deque
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    p = input().rstrip()
    n = int(input())
    text = input().rstrip()
    arr = deque(re.findall(r'\d+', text))
    isOK = True
    reverse = 0

    for ch in p :
        if ch == "R" :
            reverse += 1
        else :
            if len(arr) == 0 :
                print("error")
                isOK = False
                break
            else :
                if reverse % 2 == 1 :
                    arr.reverse()
                    reverse = 0
                arr.popleft()
    
    if reverse % 2 == 1 :
        arr.reverse()
    
    if isOK :
        print("["+",".join(arr)+"]")