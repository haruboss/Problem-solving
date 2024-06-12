def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    # DIVIDE Phase
    mid = len(arr)//2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    # CONQUER Phase (MERGE)
    return merge(left_arr, right_arr)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while (left_idx < len(left) and (right_idx < len(right))):
        if (left[left_idx] < right[right_idx]):
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result
    

print(merge_sort([2,5,1,3,-1,7,1,9,23,11,32]))