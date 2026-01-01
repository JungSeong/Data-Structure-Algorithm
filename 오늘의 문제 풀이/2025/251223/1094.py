import sys
INPUT = sys.stdin.readline

X = int(INPUT())
X = format(X, 'b')
print(X.count('1'))