import sys
from queue import Queue

input1 = sys.stdin.readlines()

num_instances = int(input1[0].strip())
num_line = 1
for _ in range(num_instances):
    cache_size = int(input1[num_line].strip())
    num_line += 2
    cache = []
    next_request = {}
    requests = input1[num_line].strip().split()
    num_line += 1
    for i in range(len(requests)):
        if requests[i] not in next_request:
            next_request[requests[i]] = Queue()
        next_request[requests[i]].put(i)
    page_faults = 0
    indices = {}
    for request in requests:
        if request not in cache:
            page_faults += 1
            if len(cache) < cache_size:
                indices[request] = (len(cache))
                cache.append(request)
            else:
                latest_request = -1
                latest_item = None
                for item in cache:
                    if next_request[item].empty():
                        latest_item = item
                        break
                    elif next_request[item].queue[0] > latest_request:
                        latest_request = next_request[item].queue[0]
                        latest_item = item
                indices[cache[-1]] = (indices[latest_item])
                cache[indices[latest_item]] = cache[-1]
                cache[-1] = latest_item
                cache.pop()
                indices[request] = len(cache)
                cache.append(request)
        next_request[request].get()
    print(page_faults)