import sys
from collections import Counter
input = sys.stdin.readline

alphabets = {chr(i) for i in range(ord('a'), ord('z')+1)}
mo = {'a','e','i','o','u'}
ja = alphabets - mo

while True :
    word = input().strip()
    isOK = True
    if word == "end" :
        break
    cnt = set(word)
    bl = cnt & mo

    if not bl :
        isOK = False

    rep_ja, rep_mo = 1, 1    
    for i in range(len(word)-1) :
        if word[i] in mo and word[i+1] in mo :
            rep_mo += 1
            rep_ja = 1
        elif word[i] in ja and word[i+1] in ja :
            rep_ja += 1
            rep_mo = 1
        else :
            rep_mo = rep_ja = 1
        if word[i] == word[i+1] and word[i] != "e" and word[i] != "o" :
            isOK = False
            break
        if rep_mo == 3 or rep_ja == 3 :
            isOK = False
            break

    if isOK :
        print(f"<{word}> is acceptable.")
    else :
        print(f"<{word}> is not acceptable.")