def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]
    
    if n == 1 :
        answer = 1
    elif n == 2 :
        answer = 2
    else :
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1) :
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        answer = dp[n]
        
    return answer