import sys
input = sys.stdin.readline

T = int(input())
dec = list(int(input().rstrip()) for _ in range(T))

for elem in dec :
    l = []
    if elem == 0 :
        print(0)
    else : 
        while elem != 0 :
            if elem % 3 == 2 :
                l.append("-")
                elem = elem // 3 + 1
            else :
                l.append(str(elem % 3))
                elem //= 3
        l.reverse()
        print("".join(l))