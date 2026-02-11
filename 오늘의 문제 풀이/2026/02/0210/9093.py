import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    sentenses = input().split()
    answer = []
    for word in sentenses :
        word = ''.join(reversed(word))
        answer.append(word)
    print(' '.join(answer))