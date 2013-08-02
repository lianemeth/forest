"""
Binary Tree implementations, recursive and iterative traversals
@author: Lucas Nemeth
"""

import weakref
from utils import Queue, Stack


def copy_node(origin, destination):
    if not (origin is None or destination is None):
        destination.key = origin.key
        destination.item = origin.item
        destination.left = origin.left
        destination.right = origin.right


class BinaryTree(object):
    '''A generic Binary Tree implementation (en.wikipedia.org/wiki/Binary_tree)
    Used as super-class to other binary trees
    '''
    def __init__(self, key=None, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right
        self._parent = None

    def __getstate__(self):
        self._parent = None
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state
        if self._left:
            self._left.parent = weakref.ref(self)
        if self._right:
            self._right.parent = weakref.ref(self)

    @property
    def parent(self):
        if self._parent:
            return self._parent()

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, val):
        self._left = val
        if not self._left is None:
            self._left._parent = weakref.ref(self)

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, val):
        self._right = val
        if not self._right is None:
            self._right._parent = weakref.ref(self)

    def get_key(self):
        """Returns the key value of the binary tree"""
        return self.key

    def __str__(self):
        return '{} : {}'.format(self.key, self.item)

    def is_leaf(self):
        return (self.left is None) and (self.right is None)

    def get_heigth(self):
        """recursive get Heigth method"""
        hl = self.left.getHeigth()
        hr = self.right.getHeigth()
        #returns the highest heigth
        if (hl > hr):
            # + 1 --> counting self
            return hl + 1
        else:
            # + 1 --> counting self
            return hr + 1

    def in_order(self, visit=None, *args, **kwargs):
        '''recursive in-order traversal.
        visit is a function. Aditional kwargs will be passed to
        the visit function.
        Returns a list.
        '''
        l = [self]
        if visit:
            visit(self, *args, **kwargs)
        if self.left:
            l = self.left.in_order(visit=visit, *args, **kwargs) + l
        if self.right:
            l += self.right.in_order(visit=visit, *args, **kwargs)
        return l

    def pre_order(self, visit=None, *args, **kwargs):
        '''recursive pre-order traversal.
        visit is a function. Aditional kwargs will be passed to
        the visit function.
        Returns a list.
        '''
        l = [self]
        if visit:
            visit(self, *args, **kwargs)
        if self.left:
            l += self.left.pre_order(visit=visit, *args, **kwargs)
        if self.right:
            l += self.right.pre_order(visit=visit, *args, **kwargs)
        return l

    def post_order(self, visit=None, *args, **kwargs):
        """recursive post-order traversal.
        visit is a function. Aditional kwargs will be passed to
        the visit function.
        Returns a list."""
        l = []
        if self.left:
            l = self.left.post_order(visit=visit, *args, **kwargs)
        if self.right:
            l = l + self.right.post_order(visit=visit, *args, **kwargs)
        if visit:
            visit(self, *args, **kwargs)
        l = l + [self]
        return l

    def breadth_first_search(self):
        """iterative Breadth First Search.
        Returns a list."""
        l = []
        queue = Queue()
        #enqueue itself
        queue.enqueue(self)
        while not queue.is_empty():
            #dequeue and gets acess to top of queue
            p = queue.dequeue()
            #append to output list
            l.append(p)
            #gets right child, if it's not empty, enqueue
            child_right = p.right
            if child_right:
                queue.enqueue(child_right)
            #gets right child, if it's not empty, enqueue
            child_left = p.left
            if child_left:
                queue.enqueue(child_left)
        return l

    def in_order_iterative(self):
        '''iterative in order method. returns a list'''
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
        """Iterative preoder method"""
        stack = Stack()
        tree = self
        queue = Queue()
        stack.push(tree)
        l = []
        while not stack.is_empty():
            tree = stack.pop()
            queue.enqueue(tree)
            if tree.right:
                stack.push(tree.right)
            if tree.left:
                stack.push(tree.left)
        while not queue.is_empty():
            l.append(queue.dequeue())
        return l

    def post_order_iterative(self):
        """Iterative post order method
        it's the same method of the preorder
        iterative, but reversed, using an
        stack in the place of the queue"""
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

    def search(self, key):
        tree = self
        while tree:
            if key == tree.get_key():
                return tree
            elif key < tree.get_key():
                tree = tree.left
            else:
                tree = tree.right

    def insert(self, key, item):
        tree = self
        aux = tree
        while tree:
            aux = tree
            if key < tree.get_key():
                tree = tree.left
            else:
                tree = tree.right
        newtree = BinarySearchTree(key, item)
        if key < aux.get_key():
            aux.left = newtree
        else:
            aux.right = newtree

    def remove_root(self):
        #The tree only have a left child
        if self.right is None and not self.left is None:
            copy_node(self.left, self)
        #The tree only have a right child
        if self.left is None and not self.right is None:
            copy_node(self.right, self)
        #The tree haves the two children
        if not self.left is None and not self.right is None:
            node = self.left
            while node:
                tree = node
                node = node.right
            old_left = self.left
            old_right = self.right
            copy_node(tree, self)
            remove_node(tree)
            self.left = old_left
            self.right = old_right


def remove_node(node):
    parent = node.parent
    if parent:
        if parent.right == node:
            parent.right = None
        else:
            parent.left = None
    else:
        node.key = None
        node.item = None


def remove_search_tree(tree, key):
    node = tree.search(key)
    if not node.right and not node.left:
        remove_node(node)
    else:
        node.remove_root()
