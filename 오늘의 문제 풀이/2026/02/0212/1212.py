import sys
input = sys.stdin.readline

num = input().rstrip()
num10 = int(num,8)
answer = bin(num10)

print(answer[2:])