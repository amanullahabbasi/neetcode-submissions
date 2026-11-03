import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph[u] holds (neighbor, time) pairs: the one-way cables out of u
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # dist holds the shortest time found for each computer
        dist = {}

        # heap of (time, computer): the smallest time always pops first
        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)
            # if this computer is already finished, this entry is stale: skip it
            if node in dist:
                continue
            # the first time a computer pops, d is its shortest time
            dist[node] = d
            # offer each neighbor a route through this computer
            for nxt, w in graph[node]:
                if nxt not in dist:
                    heapq.heappush(heap, (d + w, nxt))

        # some computer never got the signal
        if len(dist) < n:
            return -1

        # the signal is everywhere once the slowest computer has it
        longest = 0
        for node in dist:
            if dist[node] > longest:
                longest = dist[node]
        return longest