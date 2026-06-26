# test_auth.py
import unittest
from submission import get_access_level, get_student_name, BinarySearchTree


class TestStudentName(unittest.TestCase):
    def test_student_name_is_nonempty_string(self):
        name = get_student_name()
        self.assertIsInstance(name, str)
        self.assertGreater(len(name), 0)


class TestAuthSystem(unittest.TestCase):
    def test_admin_access(self):
        self.assertEqual(get_access_level("admin"), "full")

    def test_staff_access(self):
        self.assertEqual(get_access_level("staff"), "limited")

    def test_unknown_access(self):
        self.assertEqual(get_access_level("unknown"), "none")


class TestBinarySearchTree(unittest.TestCase):
    def test_search_found(self):
        tree = BinarySearchTree()
        tree.insert(50)
        tree.insert(30)
        tree.insert(70)

        for val in [50, 30, 70]:
            with self.subTest(val=val):
                found = tree.search(val)
                self.assertIsNotNone(found)
                assert found is not None
                self.assertEqual(found.val, val)

    def test_search_not_found(self):
        tree = BinarySearchTree()
        tree.insert(50)
        tree.insert(30)
        self.assertIsNone(tree.search(99))

    def test_search_empty_tree(self):
        tree = BinarySearchTree()
        self.assertIsNone(tree.search(1))

    def test_single_node(self):
        tree = BinarySearchTree()
        tree.insert(42)
        found = tree.search(42)
        self.assertIsNotNone(found)
        assert found is not None
        self.assertEqual(found.val, 42)
        self.assertEqual(tree.get_in_order(), [42])

    def test_tree_structure(self):
        """In-order traversal must produce a sorted list, validating BST ordering invariants."""
        tree = BinarySearchTree()
        for num in [50, 30, 70, 20, 40, 60, 80]:
            tree.insert(num)
        self.assertEqual(tree.get_in_order(), [20, 30, 40, 50, 60, 70, 80])

    def test_tree_structure_sorted_input(self):
        """Inserting in sorted order degrades to a linked list shape but must still satisfy BST ordering."""
        tree = BinarySearchTree()
        for num in [1, 2, 3, 4, 5]:
            tree.insert(num)
        self.assertEqual(tree.get_in_order(), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
