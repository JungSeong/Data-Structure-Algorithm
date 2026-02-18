import sys
INPUT = sys.stdin.readline

X, N = map(int, INPUT().split())
if N%2 != 0 :
    print("ERROR")
    exit(0)
if X <= 0 :
    print(0)
    exit(0)
else :
    if N==0 :
        print("INFINITE")
    else :
        if X%(N/2) == 0 :
            print(int(X/(N/2)-1))
        else :
            print(int(X/(N/2)))