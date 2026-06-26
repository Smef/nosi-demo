def get_student_name():
    """
    Return your full name as a string.

    Returns:
        str: Your full name, e.g. "Jane Smith".
    """
    raise NotImplementedError("This function is not yet implemented.")


def get_access_level(role):
    """
    Return the access level string for a given role.

    If the role is "admin" this function should return "full".
    If the role is "staff" this function should return "limited".
    For any other role, it should return "none".

    Args:
        role (str): The role of the user (e.g., "admin", "staff", "unknown").
    Returns:
        str: The access level corresponding to the role.
    """
    raise NotImplementedError("This function is not yet implemented.")


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
        """
        Recursively find the correct position and insert a new node.

        If current_node is None, a new TreeNode with the given key should be
        created and returned. Otherwise, if key is less than current_node.val,
        recurse into the left subtree; if greater, recurse into the right
        subtree. Duplicate keys should be ignored. In all cases, return
        current_node so the parent can update its child reference.

        Args:
            current_node (TreeNode or None): The node currently being examined.
            key (int): The value to insert.
        Returns:
            TreeNode: The (possibly new) node occupying this position in the tree.
        """
        raise NotImplementedError("This function is not yet implemented.")

    def search(self, key):
        """Public method to search for a key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        """
        Recursively search the tree for a node with the given key.

        If current_node is None, the key is not in the tree — return None.
        If current_node.val equals key, return current_node. Otherwise,
        recurse left if key is smaller, or right if key is larger.

        Args:
            current_node (TreeNode or None): The node currently being examined.
            key (int): The value to search for.
        Returns:
            TreeNode or None: The node whose val matches key, or None if not found.
        """
        raise NotImplementedError("This function is not yet implemented.")

    def get_in_order(self):
        """Public method to return the structural in-order traversal list."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, current_node, result):
        """
        Recursively collect node values in ascending order (Left, Root, Right).

        If current_node is None, do nothing and return. Otherwise, recurse
        into the left subtree first, then append current_node.val to result,
        then recurse into the right subtree.

        Args:
            current_node (TreeNode or None): The node currently being visited.
            result (list): The list to append values to, modified in place.
        Returns:
            None
        """
        raise NotImplementedError("This function is not yet implemented.")
