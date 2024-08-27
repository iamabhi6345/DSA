def convert_adj_matrix_to_list(self,adj_matrix):
        V = len(adj_matrix)
        adj_list = [[] for _ in range(V)]

        for i in range(V):
            for j in range(V):
                if adj_matrix[i][j] == 1 and i != j:
                    adj_list[i].append(j)

        return adj_list