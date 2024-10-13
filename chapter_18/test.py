import vertex
import undirected_graph_vertex
import dfs_traverse
import dfs
import bfs_traverse
import solution4
import solution5
import weighted_graph_vertex
import city
import dijkstra


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")

# Vertex - Directed Graph - Add adjacent vertex
alice = vertex.Vertex("alice")
bob = vertex.Vertex("bob")
cynthia = vertex.Vertex("cynthia")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
assert_equal(alice.adjacent_vertices[0].value, "bob")
assert_equal(alice.adjacent_vertices[1].value, "cynthia")

# Vertex - Undirected Graph - Add adjacent vertex
alice = undirected_graph_vertex.Vertex("alice")
bob = undirected_graph_vertex.Vertex("bob")
alice.add_adjacent_vertex(bob)
assert_equal(alice.adjacent_vertices[0].value, "bob")
assert_equal(bob.adjacent_vertices[0].value, "alice")

# Depth-first traverse
alice = vertex.Vertex("Alice")
bob = vertex.Vertex("Bob")
candy = vertex.Vertex("Candy")
derek = vertex.Vertex("Derek")
elaine = vertex.Vertex("Elaine")
fred = vertex.Vertex("Fred")
gina = vertex.Vertex("Gina")
helen = vertex.Vertex("Helen")
irena = vertex.Vertex("Irena")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)
bob.add_adjacent_vertex(fred)
fred.add_adjacent_vertex(helen)
derek.add_adjacent_vertex(gina)
gina.add_adjacent_vertex(irena)
bob.add_adjacent_vertex(alice)
candy.add_adjacent_vertex(alice)
derek.add_adjacent_vertex(alice)
elaine.add_adjacent_vertex(alice)
fred.add_adjacent_vertex(bob)
helen.add_adjacent_vertex(fred)
gina.add_adjacent_vertex(derek)
irena.add_adjacent_vertex(gina)

print("DFS Traverse")
dfs_traverse.dfs_traverse(alice, {})

# BFS traverse
print("BFS Traverse")
bfs_traverse.bfs_traverse(alice)

# DFS
print("DFS")
assert_equal(dfs.dfs(alice, "Alice", {}), alice)
assert_equal(dfs.dfs(alice, "Gina", {}), gina)
assert_equal(dfs.dfs(alice, "Jorge", {}), None)

# Solution 4 (BFS Search)
print("Solution 4")
assert_equal(solution4.bfs(alice, "Alice"), alice)
assert_equal(solution4.bfs(alice, "Gina"), gina)
assert_equal(solution4.bfs(alice, "Jorge"), None)

# Solution 5 (BFS Search)
print("Solution 5")
idris = vertex.Vertex("Idris")
talia = vertex.Vertex("Talia")
ken = vertex.Vertex("Ken")
marco = vertex.Vertex("Marco")
sasha = vertex.Vertex("Sasha")
lina = vertex.Vertex("Lina")
kamil = vertex.Vertex("Kamil")
idris.add_adjacent_vertex(talia)
talia.add_adjacent_vertex(idris)
talia.add_adjacent_vertex(ken)
ken.add_adjacent_vertex(talia)
ken.add_adjacent_vertex(marco)
marco.add_adjacent_vertex(ken)
marco.add_adjacent_vertex(sasha)
sasha.add_adjacent_vertex(marco)
sasha.add_adjacent_vertex(lina)
lina.add_adjacent_vertex(sasha)
lina.add_adjacent_vertex(kamil)
kamil.add_adjacent_vertex(lina)
kamil.add_adjacent_vertex(idris)
idris.add_adjacent_vertex(kamil)

assert_equal(solution5.shortest_path(idris, lina, {}), ["Idris", "Kamil", "Lina"])

# Weighted graph vertex
print("Weighted graph vertex")
a = weighted_graph_vertex.WeightedGraphVertex("A")
b = weighted_graph_vertex.WeightedGraphVertex("B")
a.add_adjacent_vertex(b, 100)
assert_equal(a.adjacent_vertices, {b: 100})

# City-specific vertex
print("City-specific vertex")
chicago = city.City("Chicago")
denver = city.City("Denver")
chicago.add_route(denver, 100)
assert_equal(chicago.routes, {denver: 100})

# Dijkstra's Algorithm
print("Dijkstra's Algorithm")
atlanta = city.City("Atlanta")
boston = city.City("Boston")
chicago = city.City("Chicago")
denver = city.City("Denver")
el_paso = city.City("El Paso")

atlanta.add_route(denver, 160)
atlanta.add_route(boston, 100)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)
el_paso.add_route(boston, 100)

assert_equal(dijkstra.dijkstra_shortest_path(atlanta, el_paso), ["Atlanta", "Denver", "Chicago", "El Paso"])
