adj_mat =    [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]

def convertion(adj_mat):
    #define the function convert
    adj_list = []
    for i in range(len(adj_mat)):
        neighbor_elements = []
    #create an empty list and loop through the matrix row
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] != 0:
    #loop through the ith row and check if there is and edge with the condition: edge is present when node is not equal to zero
                neighbor_elements.append(j)
        adj_list.append(neighbor_elements)
        #for every edge found a neigbor element is created and added to the adacency list.
    return adj_list

adj_list_output = convertion(adj_mat)
print(adj_list_output)
