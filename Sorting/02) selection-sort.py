# selecting the min element and putting it in the beginning
# Time complicity: O(n^2)

def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):

            # swapping the element
            if arr[i] > arr[j]:
                arr[i],  arr[j] = arr[j], arr[i]
    return arr


print(selection_sort([2,5,1,7,49,34]))
