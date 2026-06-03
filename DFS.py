def dfs(adj_matrix,node_label):# Node_label is start_node or root_node
    n=len(adj_matrix)
    stack=[]
    visited=[False]*n

    def explore(node):
        visited[node]=True
        stack.append(node)

        for nei in range(n):
            if adj_matrix[node][nei]==1 and not visited[nei]:
                explore(nei)
    
    explore(node_label)
    return stack
