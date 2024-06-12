# find the max and push the element at the end.
# Time complicity: O(n^2)

def bubble_sort(arr):
    if len(arr) < 2:
        return arr
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):

            # swapping the element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort([1,2,5,4,3, 88, 23,65]))
