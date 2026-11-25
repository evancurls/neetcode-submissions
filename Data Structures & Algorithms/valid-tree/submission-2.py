class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #must be a root node, no edges in dfs can be already seen
        if len(edges) != n - 1: return False
        adj = [[] for _ in range(n)]
        seen = {0}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        #print(adj)
        q = deque([(0, -1)])
        while q:
            curr, parent = q.popleft()
            #print(f'looking at {curr}s edges')
            for neighbor in adj[curr]:
                #print(neighbor)
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                seen.add(neighbor)
                q.append((neighbor,curr))
        return len(seen) == n
        