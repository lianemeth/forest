import unittest
from ..BinaryTree import BinaryTree, BinarySearchTree, RedBlackTree


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
        i = BinaryTree(key=17, item='n', left=a)
        g = BinaryTree(key=0, item='h', left=h, right=i)
        self.tree = g

    def test_in_order(self):
        self.assertEqual(self.tree.in_order(),
                         self.tree.in_order_iterative())
        key_list = [i.get_key() for i in self.tree.in_order()]
        self.assertEqual(key_list, [1,4,2,8,3,6,5,0,15,14,11,17])

    def test_pre_order(self):
        self.assertEqual(self.tree.pre_order(),
                         self.tree.pre_order_iterative())
        key_list = [i.get_key() for i in self.tree.pre_order()]
        self.assertEqual(key_list, [0,8,4,1,2,6,3,5,17,14,15,11])

    def test_post_order(self):
        self.assertEqual(self.tree.post_order(),
                         self.tree.post_order_iterative())
        key_list = [i.get_key() for i in self.tree.post_order()]
        self.assertEqual(key_list, [1,2,4,3,5,6,8,15,11,14,17,0])

    def test_properties(self):
        self.assertTrue(self.tree.left)
        self.assertTrue(self.tree.right)
        self.assertEqual(self.tree.left.parent, self.tree)

    def test_height(self):
        self.assertEqual(self.tree.get_height(), 4)

    def test_leaf(self):
        self.assertFalse(self.tree.is_leaf())
        self.assertTrue(self.tree.left.left.left.is_leaf())


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree(10, 'b')
        self.tree.insert(15, 'k')
        self.tree.insert(17, 'm')
        self.tree.insert(9, 'l')
        self.tree.insert(2, 'j')
        self.tree.insert(1, 'o')

    def test_search(self):
        self.assertEqual(self.tree[2].item, 'j')
        self.assertEqual(self.tree[1].item, 'o')
        self.assertIsNone(self.tree[219])

    def test_remove(self):
        del self.tree[1]
        self.assertIsNone(self.tree[1])
        del self.tree[15]
        self.assertIsNone(self.tree[15])
        del self.tree[10]
        self.assertIsNone(self.tree[10])

    def test_search_tree(self):
        def is_sorted(node):
            if node.left:
                if node.left.get_key() > node.get_key():
                    return False
            if node.right:
                if node.right.get_key() < node.get_key():
                    return False
            return True
        self.assertTrue(self.tree.pre_order(visit=is_sorted))
        
class TestRedBlacTree(unittest.TestCase):

    def setUp(self):
        self.tree = RedBlackTree(10, 'b')
        self.tree.insert(15, 'k')
        self.tree.insert(17, 'm')
        self.tree.insert(9, 'l')
        self.tree.insert(2, 'j')
        self.tree.insert(1, 'o')

    def test_search(self):
        self.assertEqual(self.tree[2].item, 'j')
        self.assertEqual(self.tree[1].item, 'o')
        self.assertIsNone(self.tree[219])

    def test_remove(self):
        del self.tree[1]
        self.assertIsNone(self.tree[1])
        del self.tree[15]
        self.assertIsNone(self.tree[15])
        del self.tree[10]
        self.assertIsNone(self.tree[10])

    def test_search_tree(self):
        def is_sorted(node):
            if node.left:
                if node.left.get_key() > node.get_key():
                    return False
            if node.right:
                if node.right.get_key() < node.get_key():
                    return False
            return True
        self.assertTrue(self.tree.pre_order(visit=is_sorted))

if __name__ == '__main__':
    unittest.main()
