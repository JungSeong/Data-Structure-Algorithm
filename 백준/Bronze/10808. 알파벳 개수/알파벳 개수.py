import sys
input = sys.stdin.readline

alphabet = input().rstrip()
nums = [0]*26

for ch in alphabet :
    idx = ord(ch)-ord('a')
    nums[idx] += 1

print(*nums)