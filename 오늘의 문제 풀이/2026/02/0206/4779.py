import sys
input = sys.stdin.readline

def Cantore(p, cur_r) :
    if p == 1 :
        return True
    left, right = p//3, p*2//3
    if cur_r<left :
        return Cantore(p//3, cur_r)
    elif cur_r>=right :
        return Cantore(p//3, cur_r-right)
    else :
        return False

while True :
    try :
        N = int(input())
        p = pow(3, N)
        answer = []

        for i in range(p) :
            if Cantore(p, i) :
                answer.append(i)

        ch = ""
        for i in range(p) :
            if i in answer :
                ch += "-"
            else :
                ch += " "
        print(ch)

    except :
        break