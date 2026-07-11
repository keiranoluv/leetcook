class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False]*n
        complete_cnt = 0

        for start in range(n):
            if visited[start] == True:
                continue
            
            stack = [start]
            visited[start] = True

            node_cnt = 0
            degree_sum = 0

            while stack:
                node = stack.pop()
                node_cnt +=1
                degree_sum += len(graph[node]) 


                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            edge_cnt = degree_sum //2
            
            if (edge_cnt == node_cnt*(node_cnt-1)//2):
                complete_cnt +=1

            
        return complete_cnt
        