class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #adjaceny list
        #visited array

        components = 0
        #makes an adjacency list for all nodes
        adj = [[] for _ in range(n)]

        #create adjaceny list
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        #print(adj)
        #marks all nodes as not visited
        visited = [False] * n

        #bfs
        def bfs(node):
            q = deque([node])
            visited[node] = True
            while q:
                cur_node = q.popleft()
                #print(f'DFS {cur_node} for origin {node}')
                for neighbor in adj[cur_node]:
                    if not visited[neighbor]:
                        #print(f'Adding {neighbor} as neighbor to {cur_node}')
                        visited[neighbor] = True
                        q.append(neighbor)
        
        for node in range(n):
            #checks if visited yet, if not then create new component
            if not visited[node]:
                bfs(node)
                components += 1

        return components

