class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()
        for course in range(len(indegree)):
            if indegree[course] == 0:
                queue.append(course)

        done = 0
        while queue:
            course = queue.popleft()
            done += 1
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return done == numCourses