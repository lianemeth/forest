"""
Binary Tree implementations, recursive and iterative traversals
@author: Lia Nemeth
"""

import weakref
from forest.utils import Queue, Stack


def copy_node(origin, destination):
    if not (origin is None or destination is None):
        destination.key = origin.key
        destination.item = origin.item
        destination.left = origin.left
        destination.right = origin.right


class BinaryTree(object):
    """
    A generic Binary Tree implementation (en.wikipedia.org/wiki/Binary_tree)
    Used as super-class to other binary trees
    """
    def __init__(self, key=None, item=None, left=None, right=None):
        """
        Constructor method
        Args:
            key - The key value of the node
            item - The item stored in the node
            left -  the left node
            right- the right  node
        """
        self.key = key
        self.item = item
        self.left = left
        self.right = right
        self._parent = None

    def __getstate__(self):
        """
        This is used if we need to pickle this tree.
        It removes the weakref to parent, because they would  be dead references
        if we were to unpikcle.
        """
        self._parent = None
        return self.__dict__

    def __setstate__(self, state):
        """
        Recreates the trees including the weakref to parent.
        """
        self.__dict__ = state
        if self._left:
            self._left.parent = weakref.ref(self)
        if self._right:
            self._right.parent = weakref.ref(self)

    @property
    def parent(self):
        """
        It uses  weakrefs to avoid memory leak
        """
        if self._parent:
            return self._parent()

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, val):
        """
        It uses  weakrefs to avoid memory leak
        """
        self._left = val
        if self._left is not  None:
            self._left._parent = weakref.ref(self)

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, val):
        """
        It uses  weakrefs to avoid memory leak
        """
        self._right = val
        if self._right is not None:
            self._right._parent = weakref.ref(self)

    def __str__(self):
        return '<{type} - {key} : {item}>'.format(type=type(self).__name__, 
                                                   key=self.key, 
                                                   item=self.item)

    def is_leaf(self):
        """
        A leaf is a node  with no children
        """
        return (self.left is None) and (self.right is None)

    def get_height(self):
        """
        Recursive get Height method
        Get lef height, get righ height, returns the  highest value + 1
        """
        hl = self.left.get_height() if self.left else 0
        hr = self.right.get_height() if self.right else 0
        # returns the highest height
        if (hl > hr):
            # + 1 --> counting self
            return hl + 1
        else:
            # + 1 --> counting self
            return hr + 1

    def in_order(self, visit=None, *args, **kwargs):
        """
        Recursive in-order traversal.
        Args:
            visit - *optional* A callable object
            *args - Will be passed to visit
            **kwargs -  Will be passed to visit
        Returns:
            a list containing all nodes in order
        """
        l = []
        if self.left:
            l += self.left.in_order(visit=visit, *args, **kwargs)
        if visit:
            visit(self, *args, **kwargs)
        l += [self]
        if self.right:
            l += self.right.in_order(visit=visit, *args, **kwargs)
        return l

    def __iter__(self):
        """
        Default iterator returns a generator in order traversal
        """
        if self.left:
            for node in self.left:
                yield node
        yield self
        if self.right:
            for node in self.right:
                yield node

    def pre_order(self, visit=None, *args, **kwargs):
        """
        Recursive pre-order traversal.
        Args:
            visit - *optional* A callable object
            *args - Will be passed to visit
            **kwargs -  Will be passed to visit
        Returns:
            a list containing all nodes pre order
        """
        l = [self]
        if visit:
            visit(self, *args, **kwargs)
        if self.left:
            l += self.left.pre_order(visit=visit, *args, **kwargs)
        if self.right:
            l += self.right.pre_order(visit=visit, *args, **kwargs)
        return l

    def post_order(self, visit=None, *args, **kwargs):
        """
        Recursive post-order traversal.
        Args:
            visit - *optional* A callable object
            *args - Will be passed to visit
            **kwargs -  Will be passed to visit
        Returns:
            a list containing all nodes post order
        """
        l = []
        if self.left:
            l += self.left.post_order(visit=visit, *args, **kwargs)
        if self.right:
            l += self.right.post_order(visit=visit, *args, **kwargs)
        if visit:
            visit(self, *args, **kwargs)
        l += [self]
        return l

    def breadth_first_search(self, key):
        """
        Iterative Breadth First Search  algorithm.
        Args:
            key - The node key
        Returns:
            The item if key is found, or None if not found any item.
        """
        queue = Queue()
        # enqueue itself
        queue.enqueue(self)
        while not queue.is_empty():
            p = queue.dequeue()
            if p.key == key:
                # found the item
                return p
            # enqueue children
            if p.right is not None:
                queue.enqueue(p.right)
            if p.left is not None:
                queue.enqueue(p.left)

    def in_order_iterative(self):
        """
        Iterative in order method. returns a list of all  nodes.
        """
        stack = Stack()
        tree = self
        l = []
        while tree or not stack.is_empty():
            if tree:
                stack.push(tree)
                tree = tree.left
            else:
                tree = stack.pop()
                l.append(tree)
                tree = tree.right
        return l

    def pre_order_iterative(self):
        """
        Iterative pre order method. returns a list of all  nodes.
        """
        stack = Stack()
        tree = self
        output = Queue()
        stack.push(tree)
        l = []
        while not stack.is_empty():
            tree = stack.pop()
            output.enqueue(tree)
            if tree.right:
                stack.push(tree.right)
            if tree.left:
                stack.push(tree.left)
        while not output.is_empty():
            l.append(output.dequeue())
        return l

    def post_order_iterative(self):
        """
        Iterative post order method
        Note: it's the same method of the preorder iterative,
               but using a stack in place of a queue
        """
        stack = Stack()
        output = Stack()
        tree = self
        stack.push(tree)
        l = []
        while not stack.is_empty():
            tree = stack.pop()
            output.push(tree)
            if tree.left:
                stack.push(tree.left)
            if tree.right:
                stack.push(tree.right)
        while not output.is_empty():
            l.append(output.pop())
        return l


class BinarySearchTree(BinaryTree):
    """
    A Binary Search Tree implementation (en.wikipedia.org/wiki/Binary_tree)
    This implementation doesn't take care of any balancing of the  tree.
    """

    def search(self, key):
        """
        Classic search algorithm on BST
        Args:
          key - The key for the node that is being searched
        """
        tree = self
        while tree:
            if key == tree.key:
                return tree
            elif key < tree.key:
                tree = tree.left
            else:
                tree = tree.right

    def __getitem__(self, key):
        return self.search(key)

    def insert(self, key, item):
        """
        Insert a new item in the BST
        Args:
            key - the item key
            item - the item value
        """
        tree = self
        aux = tree
        while tree:
            aux = tree
            if key < tree.key:
                tree = tree.left
            else:
                tree = tree.right
        newtree = BinarySearchTree(key, item)
        if key < aux.key:
            aux.left = newtree
        else:
            aux.right = newtree
        return newtree

    def __setitem__(self, key, val):
        self.insert(key, val)

    def __delitem__(self, key):
        self.remove(key)

    def remove(self, key):
        """
        Remove an item of the tree.
        """
        node = self.search(key)
        if not node.right and not node.left:
            node.remove_node()
        else:
            node.remove_root()

    def remove_node(self):
        """
        Remove a node that is  not the root of the tree.
        """
        parent = self.parent
        if parent:
            if parent.right == self:
                parent.right = None
            else:
                parent.left = None
        else:
            self.key = None
            self.item = None

    def remove_root(self):
        # The tree only has a left child
        if self.right is None and self.left is not None:
            copy_node(self.left, self)
        # The tree only has a right child
        if self.left is None and self.right is not None:
            copy_node(self.right, self)
        # The tree has two children
        if self.left is None and self.right is not None:
            node = self.left
            while node:
                tree = node
                node = node.right
            old_left = self.left
            old_right = self.right
            copy_node(tree, self)
            tree.remove_node()
            self.left = old_left
            self.right = old_right


class RedBlackTree(BinarySearchTree):

    def __init__(self, key=None, item=None, left=None, right=None, black=True):
        super(RedBlackTree, self).__init__(key=key, item=item, left=left,
                                           right=right)
        self.black = black

    def insert(self, key, item):
        newtree = super(RedBlackTree, self).insert(key, item)
        # new nodes are painted red
        newtree.black = False
        return newtree
