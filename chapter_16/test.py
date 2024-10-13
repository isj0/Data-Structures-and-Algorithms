import heap


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Insertion of root node
print("Insertion of root node")
h = heap.Heap()
h.insert(100)
assert_equal(h.root_node(), 100)

# Insertion of second node that is less than root
print("Insertion of second node that is less than root")
h.insert(88)
assert_equal(h.root_node(), 100)

# Insertion of new node that is greater than root
print("Insertion of new node that is greater than root")
h.insert(101)
assert_equal(h.root_node(), 101)

# Last node of multi-level heap
print("Last node of multi-level heap")
h = heap.Heap()
h.insert(100)
h.insert(88)
h.insert(25)
h.insert(87)
h.insert(16)
h.insert(8)
h.insert(12)
h.insert(86)
h.insert(50)
h.insert(2)
h.insert(15)
h.insert(3)
assert_equal(h.root_node(), 100)
assert_equal(h.last_node(), 3)

# Trickle up node
print("Trickle up node")
h.insert(40)
assert_equal(h.last_node(), 8)

# Deletion
print("Deletion / Pop")
h = heap.Heap()
h.insert(100)
h.insert(88)
h.insert(25)
h.insert(87)
h.insert(16)
h.insert(8)
h.insert(12)
h.insert(86)
h.insert(50)
h.insert(2)
h.insert(15)
h.insert(3)
popped_node = h.pop()
assert_equal(popped_node, 100)
assert_equal(h.root_node(), 88)
assert_equal(h.last_node(), 15)
