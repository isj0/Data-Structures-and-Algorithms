import node
import linked_list
import doubly_linked_list
import queue
import solution5


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Node
print("Node")
node_1 = node.Node("once")
node_2 = node.Node("upon")
node_3 = node.Node("a")
node_4 = node.Node("time")
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4
assert_equal(node_1.data, "once")
assert_equal(node_1.next_node, node_2)
assert_equal(node_1.next_node.next_node.next_node, node_4)

# Linked List - Basic
print("Linked List - Basic")
list = linked_list.LinkedList(node_1)
assert_equal(list.first_node, node_1)
assert_equal(list.first_node.next_node, node_2)

# Linked List - Read
print("Linked List - Read")
assert_equal(list.read(2), "a")
assert_equal(list.read(6), None)

# Linked List - Search
print("Linked List - Search")
assert_equal(list.search("a"), 2)
assert_equal(list.search("happily"), None)

# Linked List - Insert
print("Linked List - Insert")
list.insert(4, "there")
assert_equal(list.search("there"), 4)
list.insert(0, "Hello!")
assert_equal(list.search("Hello!"), 0)

# Linked List - Delete
print("Linked List - Delete")
list.delete(0)
assert_equal(list.search("once"), 0)
list.delete(4)
assert_equal(list.read(4), None)
assert_equal(list.read(3), "time")

# Linked List - Append
print("Linked List - Append")
new_list = linked_list.LinkedList()
new_list.append(1)
new_list.append(2)
assert_equal(new_list.read(0), 1)
assert_equal(new_list.read(1), 2)
assert_equal(new_list.read(2), None)

# Linked List - Recursive Append
print("Linked List - Recursive Append")
new_list = linked_list.LinkedList()
new_list.recursive_append(1)
new_list.recursive_append(2)
new_list.recursive_append(3)
assert_equal(new_list.read(0), 1)
assert_equal(new_list.read(1), 2)
assert_equal(new_list.read(2), 3)
assert_equal(new_list.read(3), None)

# Doubly Linked List - Append
print("Doubly Linked List - Append")
dlist = doubly_linked_list.DoublyLinkedList()
dlist.append("A")
assert_equal(dlist.first_node.data, "A")
assert_equal(dlist.last_node.data, "A")
dlist.append("B")
dlist.append("C")
assert_equal(dlist.first_node.data, "A")
assert_equal(dlist.last_node.data, "C")

# Doubly Linked List - pop head
print("Doubly Linked List - pop head")
popped_node = dlist.pop_head()
assert_equal(popped_node.data, "A")
assert_equal(dlist.first_node.data, "B")
assert_equal(dlist.last_node.data, "C")
assert_equal(dlist.first_node.previous_node, None)

# Queue
print("Queue")
queue = queue.Queue()
assert_equal(queue.read(), None)
queue.enqueue("A")
queue.enqueue("B")
assert_equal(queue.read(), "A")
popped_node = queue.dequeue()
assert_equal(popped_node, "A")
assert_equal(queue.read(), "B")

# Solution 1 : once upon a time
print("Solution 1")
list.print_list()

# Solution 2 : C B A
print("Solution 2")
dlist.reverse_print()

# Solution 3
print("Solution 3")
assert_equal(list.last(), "time")

# Solution 3b
print("Solution 3b")
assert_equal(list.recursive_last(), "time")

# Solution 4
print("Solution 4")
list.reverse()
assert_equal(list.last(), "once")
assert_equal(list.first_node.data, "time")
list.reverse()  # Preparing for next test

# Solution 5
print("Solution 5")
solution5.delete_node(node_3)
assert_equal(list.read(0), "once")
assert_equal(list.read(1), "upon")
assert_equal(list.read(2), "time")
