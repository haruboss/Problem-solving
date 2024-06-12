# traverse array one by one element to find the element.
# Time Complicity: O(n)

def linear_search(nums, n):
    if nums is None:
        return None
    for number in range(len(nums)):
        if (nums[number] == n):
            return number
    return None

print("Number found at index: ", linear_search([1,2,3,4,5,5], 2))

