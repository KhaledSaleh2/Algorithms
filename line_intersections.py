import sys
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, pair):
        heapq.heappush(self.heap, pair)

    def pop(self):
        return heapq.heappop(self.heap)
lines = sys.stdin.readlines()

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

num_instances = int(lines[0].strip())
line_num = 1
for _ in range(num_instances):
    num_points = int(lines[line_num].strip())
    line_num += 1
    pq = PriorityQueue()
    array = []
    num_intersections = 0
    for i in range(num_points):
        x = int(lines[line_num + i].strip())
        y = int(lines[line_num + i + num_points].strip())
        pq.push((x, y))
    while len(pq.heap) > 0:
        line = pq.pop()
        point = line[1]
        array.append(point)
    _, num_intersections = merge_sort(array, 0)
    print(num_intersections)
    line_num += num_points * 2