import unittest
from Ntree import *


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
            self.assertTrue(node in self.tree.all_items)
        self.tree.traversal(in_here)


if __name__ == '__main__':
    unittest.main()
