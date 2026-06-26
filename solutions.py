def get_student_name():
    """
    Function to get the student's name.
    Returns:
        str: The name of the student.
    """
    NotImplementedError("This function is not yet implemented.")


def get_access_level(role):
    """
    Function to get the access level based on the role.

    If the role is "admin" this function should return "full".
    If the role is "staff" this function should return "limited".
    For any other role, it should return "none".

    Args:
        role (str): The role of the user (e.g., "admin", "staff", "unknown").
    Returns:
        str: The access level corresponding to the role.
    """
    if role == "admin":
        return "full"
    elif role == "staff":
        return "limited"
    else:
        return "none"


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Public method to insert a key into the BST."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Helper method to recursively find the right spot and insert."""
        if current_node is None:
            return TreeNode(key)

        if key < current_node.val:
            current_node.left = self._insert_recursive(current_node.left, key)
        elif key > current_node.val:
            current_node.right = self._insert_recursive(current_node.right, key)

        return current_node

    def search(self, key):
        """Public method to search for a key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        """Helper method to recursively traverse and search the tree."""
        if current_node is None or current_node.val == key:
            return current_node

        if key < current_node.val:
            return self._search_recursive(current_node.left, key)
        return self._search_recursive(current_node.right, key)

    def get_in_order(self):
        """Public method to return the structural in-order traversal list."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, current_node, result):
        """Helper method to collect values sequentially (Left, Root, Right)."""
        if current_node:
            self._in_order_recursive(current_node.left, result)
            result.append(current_node.val)
            self._in_order_recursive(current_node.right, result)
