def search_number(nums, n):
    if nums is []:
        return -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        m = (start+end) // 2

        if nums[m] == n:
            return m
        elif nums[m] < n:
            start = m+1
        else:
            end = m-1
    return -1


print(search_number([21, 22, 23],22))
