import sys
input = sys.stdin.readline

word = input().rstrip()

word = word.replace("XXXX", "AAAA")
word = word.replace("XX", "BB")

if "X" in word :
    print(-1)
    sys.exit(0)
        
print(word)