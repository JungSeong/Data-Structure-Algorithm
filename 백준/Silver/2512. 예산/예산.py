import sys
input = sys.stdin.readline

N = int(input())
costs = list(map(int, input().split()))
M = int(input())

if sum(costs) <= M :
    print(max(costs))
else :
    costs.sort()
    min_num, max_num = 1, costs[-1]

    def binary_search(min_num, max_num, cur_best) :
        if min_num > max_num :
            return cur_best
        mid = (min_num+max_num)//2
        cost_sum = 0
        for cost in costs :
            cost_sum += min(cost, mid)

        if cost_sum <= M :
            return binary_search(mid+1, max_num, mid)
        else :
            return binary_search(min_num, mid-1, cur_best)

    print(binary_search(min_num, max_num, 0))
