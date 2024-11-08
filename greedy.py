import sys
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, pair):
        heapq.heappush(self.heap, pair)

    def pop(self):
        return heapq.heappop(self.heap)

user_input = sys.stdin.readlines()

num_instances = int(user_input[0].strip())
line_num = 1
for _ in range(num_instances):
    num_pairs = int(user_input[line_num].strip())
    line_num += 1
    max_jobs = 1
    pq = PriorityQueue()
    for i in range(num_pairs):
        line = user_input[line_num].strip().split()
        pq.push((int(line[1]), int(line[0])))
        line_num += 1
    end_time = pq.pop()[0]
    while pq.heap:
        pair = pq.pop()
        if pair[1] >= end_time:
            max_jobs += 1
            end_time = pair[0]
    print(max_jobs)