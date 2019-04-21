import unittest
from forest.NaryTree import NaryTree


class TestNaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = NaryTree(key='1')
        branch1 = self.tree.add_child(key='1.1', item=0)
        branch2 = self.tree.add_child(key='1.2', item=0)
        branch3 = self.tree.add_child(key='1.3', item=0)
        branch11 = branch1.add_child(key='1.1.1', item=0)
        branch12 = branch1.add_child(key='1.1.2', item=0)
        branch21 = branch2.add_child(key='1.2.1', item=0)
        branch22 = branch2.add_child(key='1.2.2', item=0)
        branch31 = branch3.add_child(key='1.3.1', item=0)
        self.all_items = [self.tree, branch1, branch2, branch3, branch11,
                          branch12, branch21, branch22, branch31]

    def test_traversal(self):
        def in_here(node):
            self.assertTrue(node in self.all_items)
        self.tree.traversal(in_here)

    def test_iterator(self):
        for node in self.tree:
            self.assertTrue(node in self.all_items)

    def test_height(self):
        self.assertEqual(self.tree.get_height(), 3)

    def test_leaf(self):
        self.assertFalse(self.tree.is_leaf())
        self.assertTrue(self.all_items[8].is_leaf())

if __name__ == '__main__':
    unittest.main()
