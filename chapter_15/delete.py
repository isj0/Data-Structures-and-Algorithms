def replace_with_successor_node(node):
    successor_node = node.right_child

    if not successor_node.left_child:
        node.value = successor_node.value
        node.right_child = successor_node.right_child
        return

    while successor_node.left_child:
        parent_of_successor_node = successor_node
        successor_node = successor_node.left_child
    
    if successor_node.right_child:
        parent_of_successor_node.left_child = successor_node.right_child
    else:
        parent_of_successor_node.left_child = None

    node.value = successor_node.value
    return successor_node

def delete(value_to_delete, node):
    current_node = node
    parent_of_current_node = None
    node_to_delete = None

    while current_node:
        if current_node.value == value_to_delete:
            node_to_delete = current_node
            break

        parent_of_current_node = current_node
        if value_to_delete < current_node.value:
            current_node = current_node.left_child
        elif value_to_delete > current_node.value:
            current_node = current_node.right_child
    
    if not node_to_delete:
        return None

    if node_to_delete.left_child and node_to_delete.right_child:     
        replace_with_successor_node(node_to_delete)        
    else:  # deleted node has 0 or 1 children

        child_of_deleted_node = (node_to_delete.left_child or
                                node_to_delete.right_child)
        
        if not parent_of_current_node:
            node_to_delete.value = child_of_deleted_node.value
            node_to_delete.left_child = child_of_deleted_node.left_child
            node_to_delete.right_child = child_of_deleted_node.right_child
        elif node_to_delete == parent_of_current_node.left_child:
            parent_of_current_node.left_child = child_of_deleted_node
        elif node_to_delete == parent_of_current_node.right_child:
            parent_of_current_node.right_child = child_of_deleted_node

    return node_to_delete
