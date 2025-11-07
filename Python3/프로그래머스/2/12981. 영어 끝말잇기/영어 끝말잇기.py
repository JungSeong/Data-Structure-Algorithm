# 탈락하는 사람의 번호 : 인덱스 % 사람 수 + 1, 차례 : 인덱스 // 사람 수 + 1

def failed(n, idx) :
    print(n, idx)
    return [idx%n+1, idx//n+1]

def solution(n, words):
    answer = [0,0]
    s = set()
    
    for i in range(len(words)) :
        if words[i] in s :
            answer = failed(n, i)
            return answer
        else :
            s.add(words[i])
            if i > 0 :
                if words[i-1][-1] != words[i][0] :
                    answer = failed(n, i)
                    return answer

    return answer