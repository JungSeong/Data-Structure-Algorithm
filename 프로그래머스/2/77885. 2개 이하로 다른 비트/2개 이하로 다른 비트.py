def solution(numbers):
    answer = []
    for row in numbers :
        if row % 2 == 0 :
            answer.append(row+1)
        else :
            b_r = '0' + format(row, 'b')
            l = list(ch for ch in b_r)
            for i in range(len(l)-1, -1, -1) :
                if l[i] == '0' :
                    l[i] = '1'
                    l[i+1] = '0'
                    break
            answer.append(int(''.join(l), 2))
            
    return answer