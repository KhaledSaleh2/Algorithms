import sys

def merge(left, right, num_inversions):
    sorted_array = []
    left_index = 0
    right_index = 0
    while left_index <= len(left) - 1 and right_index <= len(right) - 1:
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            num_inversions += len(left) - left_index
            right_index += 1
    if left_index < len(left):
        for i in range(left_index, len(left)):
            sorted_array.append(left[i])
    elif right_index < len(right):
        for i in range(right_index, len(right)):
            sorted_array.append(right[i])
    return sorted_array, num_inversions

def merge_sort(array, num_inversions):
    if len(array) <= 1:
        return array, num_inversions
    midpoint = int(len(array) // 2)
    left_array = array[:midpoint]
    right_array = array[midpoint:]
    num_inversions_left = num_inversions
    num_inversions_right = num_inversions
    left_array, new_num_inversions_left = merge_sort(left_array, num_inversions)
    right_array, new_num_inversions_right = merge_sort(right_array, num_inversions)
    num_inversions_left += new_num_inversions_left
    num_inversions_right += new_num_inversions_right
    sorted_array, new_num_inversions = merge(left_array, right_array, num_inversions_left + num_inversions_right)
    num_inversions += new_num_inversions
    return sorted_array, num_inversions

lines = sys.stdin.readlines()
num_instances = int(lines[0].strip())
num_line = 1

for _ in range(num_instances):
    array = []
    num_line += 1
    line = lines[num_line].strip().split()
    num_line += 1
    for item in line:
        array.append(int(item))
    sorted_array, inversions = merge_sort(array, 0)
    print(inversions)

