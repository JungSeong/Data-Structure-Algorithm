import sys
input = sys.stdin.readline

num = int(input().rstrip(),2)
print(oct(num)[2:])