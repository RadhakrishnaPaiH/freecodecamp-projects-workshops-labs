def adjacency_list_to_matrix(dic):
    n=len(dic)
    
    matrix=[[0 for _ in range(n)] for _ in range(n)]

    for node,neighbors in dic.items():
        for neighbor in neighbors:
            matrix[node][neighbor]=1
    
    for row in matrix:
        print(row)
    return matrix
