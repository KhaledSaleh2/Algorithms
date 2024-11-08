import sys

class Job:
    def __init__(self, start_time, end_time, value):
        self.start = start_time
        self.end = end_time
        self.weight = value

def find_index(array, end_index, start_time):
    low = 0
    high = end_index - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid][1] <= start_time:
            if mid == end_index - 1 or array[mid+1][1] > start_time:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -2


num_instances = int(input())
for _ in range(num_instances):
    num_jobs = int(input())
    jobs = []
    for __ in range(num_jobs):
        vals = input().strip().split()
        jobs.append(Job(int(vals[0]), int(vals[1]), int(vals[2])))
    sorted_jobs = sorted(jobs, key=lambda job: job.end)
    max_weight = [0] * num_jobs
    max_weight[0] = (sorted_jobs[0].weight, sorted_jobs[0].end)
    for i in range(1, num_jobs):
        excluded_weight = max_weight[i-1][0]
        index = find_index(max_weight, i, sorted_jobs[i].start)
        end_time = sorted_jobs[i].end
        if index != -2:
            included_weight = sorted_jobs[i].weight + max_weight[index][0]
        else:
            included_weight = sorted_jobs[i].weight
        if included_weight == excluded_weight:
            end_time = min(end_time, max_weight[i-1][1])
        max_weight[i] = (max(excluded_weight, included_weight), end_time)
    print(max_weight[num_jobs - 1][0])