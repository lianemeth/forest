import unittest
from ..BinaryTree import (BinaryTree, remove_search_tree,
        BinarySearchTree)


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        #set up a test binary tree
        aux1 = BinaryTree(key=1, item='a')
        aux2 = BinaryTree(key=2, item='b')
        a = BinaryTree(key=4, item='c', left=aux1, right=aux2)
        aux1 = BinaryTree(key=3, item='c')
        aux2 = BinaryTree(key=5, item='a')
        f = BinaryTree(key=6, item='g', left=aux1, right=aux2)
        h = BinaryTree(key=8, item='n', left=a, right=f)
        aux1 = BinaryTree(key=15, item='k')
        aux2 = BinaryTree(key=11, item='l')
        a = BinaryTree(key=14, item='c', left=aux1, right=aux2)
        aux1 = BinaryTree(key=13, item='t')
        aux2 = BinaryTree(key=12, item='p')
        f = BinaryTree(key=16, item='q', left=aux1, right=aux2)
        i = BinaryTree(key=17, item='n', left=a, right=f)
        g = BinaryTree(key=0, item='h', left=h, right=i)
        self.tree = g

    def test_in_order(self):
        self.assertEqual(self.tree.in_order(), self.tree.in_order_iterative())

    def test_pre_order(self):
        self.assertEqual(self.tree.pre_order(),
                         self.tree.pre_order_iterative())

    def test_post_order(self):
        self.assertEqual(self.tree.post_order(),
                         self.tree.post_order_iterative())


class TestBinarySearchTree(unittest.TestCase):

    #TODO assert tree is sorted method

    def setUp(self):
        self.a = BinarySearchTree(10, 'b')
        self.a.insert(15, 'k')
        self.a.insert(17, 'm')
        self.a.insert(9, 'l')
        self.a.insert(2, 'j')
        self.a.insert(1, 'o')

    def test_search(self):
        self.assertTrue(self.a.search(2))
        self.assertTrue(self.a.search(1))
        self.assertIsNone(self.a.search(219))

    def test_remove(self):
        remove_search_tree(self.a, 1)
        self.assertIsNone(self.a.search(1))
        remove_search_tree(self.a, 15)
        self.assertIsNone(self.a.search(15))
        remove_search_tree(self.a, 10)
        self.assertIsNone(self.a.search(10))

if __name__ == '__main__':
    unittest.main()
