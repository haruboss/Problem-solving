
# ex fibonacci(4) = 0 1 1 2 3, for 
# solving fibonacci problem using DP "tabulation" technique
# SC: O(1) constant space
# TC:  O(n) running time 
def fibonacci(n):
    if (n <= 1):
        return n
    
    # start "tabulation" technique
    prev2 = 0
    prev = 1
    for _ in range(2,n+1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev
    # end "tabulation"

    # start "memorization" technique
    dp = [-1 for i in range(n+1)]
    if(dp[n] != -1):
        return dp[n]
    dp[n] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n]
    # end memorization

print(fibonacci(7))

# 0 1 1 2