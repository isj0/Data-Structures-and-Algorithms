import tree_node
import search
import insert
import delete
import preorder_traversal
import in_order_traversal
import postorder_traversal
import solution3


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Tree Node - Basic
print("BST basic")
node1 = tree_node.TreeNode(25)
node2 = tree_node.TreeNode(75)
root = tree_node.TreeNode(50, node1, node2)
assert_equal(root.value, 50)
assert_equal(root.right_child.value, 75)
assert_equal(root.left_child.value, 25)

# BST search
print("BST search")
assert_equal(search.search(50, root), root)
assert_equal(search.search(75, root), node2)
assert_equal(search.search(25, root), node1)
assert_equal(search.search(100, root), None)
assert_equal(search.search(0, root), None)

# BST insertion
print("BST insertion")

root = tree_node.TreeNode(50)
insert.insert(25, root)
insert.insert(75, root)
insert.insert(60, root)
insert.insert(100, root)
insert.insert(90, root)
insert.insert(5, root)
insert.insert(40, root)
assert_equal(search.search(50, root).value, 50)
assert_equal(search.search(25, root).value, 25)
assert_equal(search.search(75, root).value, 75)
assert_equal(search.search(60, root).value, 60)
assert_equal(search.search(100, root).value, 100)
assert_equal(search.search(90, root).value, 90)
assert_equal(search.search(5, root).value, 5)
assert_equal(search.search(40, root).value, 40)

# BST - delete
root = tree_node.TreeNode(50)
insert.insert(25, root)
insert.insert(75, root)
insert.insert(10, root)
insert.insert(33, root)
insert.insert(4, root)
insert.insert(11, root)
insert.insert(30, root)
insert.insert(40, root)
insert.insert(56, root)
insert.insert(89, root)
insert.insert(52, root)
insert.insert(61, root)
insert.insert(82, root)
insert.insert(95, root)

# Delete node from bottom level
print("Delete node from bottom level")
assert_equal(search.search(4, root).value, 4)
delete.delete(4, root)
delete.delete(44, root)
assert_equal(search.search(4, root), None)

# Delete node with a right child
print("Delete node with only right child")
assert_equal(search.search(10, root).value, 10)
delete.delete(10, root)
assert_equal(search.search(10, root), None)
assert_equal(search.search(25, root).left_child.value, 11)

# Delete node with a left child
print("Delete node with only left child")
delete.delete(40, root)
delete.delete(33, root)
assert_equal(search.search(33, root), None)
assert_equal(search.search(25, root).right_child.value, 30)

# Delete root node of tree when successor node has no children
print("Delete root node of tree when successor node has no children")
assert_equal(search.search(50, root).value, 50)
new_root = delete.delete(50, root)
assert_equal(new_root.value, 52)
assert_equal(search.search(50, root), None)
assert_equal(search.search(56, root).left_child, None)
assert_equal(new_root.right_child.value, 75)

# Delete root node of tree when successor node has a right child
print("Delete root node of complex tree when successor node has a right child")
new_root = delete.delete(52, root)
assert_equal(new_root.value, 56)
assert_equal(search.search(52, root), None)
assert_equal(search.search(75, root).left_child.value, 61)

# Delete node of tree when successor node is the right child
print("Delete node of tree when successor node is the right child")
root = tree_node.TreeNode(50)
insert.insert(25, root)
insert.insert(75, root)
insert.insert(89, root)
insert.insert(90, root)
insert.insert(95, root)
new_root = delete.delete(50, root)
assert_equal(new_root.value, 75)
assert_equal(new_root.right_child.value, 89)

# Delete root with one child
print("Delete root with one child")
root = tree_node.TreeNode(50)
insert.insert(75, root)
insert.insert(89, root)
insert.insert(90, root)
insert.insert(95, root)
new_root = delete.delete(50, root)
assert_equal(new_root.value, 75)
assert_equal(new_root.right_child.value, 89)

# Preorder traversal
print("Preorder traversal")
root = tree_node.TreeNode(5)
insert.insert(2, root)
insert.insert(7, root)
insert.insert(1, root)
insert.insert(3, root)
insert.insert(6, root)
insert.insert(8, root)
preorder_traversal.traverse_and_print(root)

# Inorder traversal
print("Inorder traversal")
in_order_traversal.traverse_and_print(root)

# Postorder traversal
print("Postorder traversal")
postorder_traversal.traverse_and_print(root)

# Solution 3
print("Solution 3")
assert_equal(solution3.max(root), 8)

