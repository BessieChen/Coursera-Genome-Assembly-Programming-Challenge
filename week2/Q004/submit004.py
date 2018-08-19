# Uses python3
from collections import defaultdict

default_read = 5396

reads_list = []
for _ in range(default_read):
    reads_list.append(input())
adj = defaultdict(list)
id = 0
for read in reads_list:
    adj[read[:-1]].append((read[1:],id))
    id += 1

path = [reads_list[0][:-1]]
already_visited = set()

while len(already_visited)<len(reads_list):
    for i, node in enumerate(path):
        allVisited = True
        for next in adj[node]:
            if next[1] not in already_visited:
                allVisited = False
                break
        if allVisited: continue
        new_cycle = [node]
        current = node
        find_Next = True
        while find_Next:
            find_Next = False
            for next in adj[current]:
                if next[1] not in already_visited:
                    already_visited.add(next[1])
                    new_cycle.append(next[0])
                    current = next[0]
                    find_Next = True
                    break
        break
    path = path[:i]+new_cycle+path[i+1:]
cycle = ""

for node in path:
    cycle += node[0]
print(cycle[:-1])
