def dfs(vertex, search_value, visited_vertices):
    visited_vertices[vertex.value] = True

    if vertex.value == search_value:
        return vertex

    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value == search_value:
            return adjacent_vertex

        if not visited_vertices.get(adjacent_vertex.value):
            vertex_we_are_searching_for = dfs(adjacent_vertex, 
                                              search_value, 
                                              visited_vertices)
            if vertex_we_are_searching_for:
                return vertex_we_are_searching_for

    return None
