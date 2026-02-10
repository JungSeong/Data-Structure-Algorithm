import sys
input = sys.stdin.readline

L = int(input())
r = 31
M = 1234567891

chr = input().rstrip()
answer = 0

for i in range(len(chr)) :
    answer += (ord(chr[i])-ord('a')+1)*(r**i)%M

print(answer)