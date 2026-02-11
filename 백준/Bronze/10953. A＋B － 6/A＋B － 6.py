import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    chr = input().rstrip()
    chr = chr.split(',')
    print(sum(map(int, chr)))