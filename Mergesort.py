def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    middle_index = len(my_list)//2
    left_list = my_list[:middle_index]
    right_list = my_list[middle_index :]
    left_sorted = merge_sort(left_list)
    right_sorted = merge_sort(right_list)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    while(left and right):
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    
    while len(left) >=1:
        result.append(left[0])
        left.pop(0)
    while len(right) >=1:
        result.append(right[0])
        right.pop(0)
    return list(result)


numbers = [8,9,5,2,8,4,2]
print(merge_sort(numbers))            
