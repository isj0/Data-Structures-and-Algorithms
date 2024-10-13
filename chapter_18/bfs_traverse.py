import queue_implementation


def bfs_traverse(starting_vertex):
    queue = queue_implementation.Queue()

    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.enqueue(starting_vertex)

    while queue.read():
        current_vertex = queue.dequeue()
        print(current_vertex.value)

        for adjacent_vertex in current_vertex.adjacent_vertices:

            if not visited_vertices.get(adjacent_vertex.value):
                visited_vertices[adjacent_vertex.value] = True
                queue.enqueue(adjacent_vertex)
