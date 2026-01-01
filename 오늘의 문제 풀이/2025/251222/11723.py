import sys
INPUT = sys.stdin.readline

M = int(INPUT())
bit = 0
for i in range(M) :
    op = list(INPUT().split())

    if len(op) != 1 :
        x = int(op[1])
    oper = op[0]

    if oper == "add" :
        bit |= (1 << x)
    elif oper == "remove" :
        bit &= ~(1 << x)
    elif oper == "check" :
        if bit & (1 << x) == 0 :
            print("0")
        else :
            print("1")
    elif oper == "toggle" :
        if bit & (1 << x) == 0 :
            bit |= (1<<x)
        else :
            bit &= ~(1 << x)
    elif oper == "all" :
        bit = (1 << 21) - 1
    elif oper == "empty" :
        bit = 0