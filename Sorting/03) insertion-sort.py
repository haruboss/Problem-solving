
# https://www.youtube.com/watch?v=R_wDA-PmGE4
# push min el at the start by split the arr 
# Time Complicity: O(n^2)

def insertion_sort(arr):
    if len(arr) < 2:
        return arr
    
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            
            # swapping the element
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


print(insertion_sort([2, 1, 4,22, 43, 11]))

