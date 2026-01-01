import sys
INPUT = sys.stdin.readline

N = int(INPUT())
students = []
M_max = 0
idx = 0

for i in range(3) :
    M, G = map(int, INPUT().split())
    students.append([M, G])
    M_max = max(M_max, M)
    if M_max == M :
        idx = i

if M_max != N - students[idx][1] or students[idx][1] != N - students[idx][0] :
    print(0)
else :
    print(1)
    print(f"{students[1][1]} {students[2][1]}")
    print(f"{students[1][0]} 0")
    print(f"{students[2][0]} 0")