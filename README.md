forest
======

Python Trees:
* Binary Tree
* Binary Search Tree
* N-ary Tree

## Binary Tree

```python
from forest.BinaryTree import BinaryTree

tree = BinaryTree(key=1, item='object',
                  left=BinaryTree(key=2, item='left'),
                  right=BinaryTree(key=3, item='right'),
)

def do_something(node):
    print node

tree.pre_order(visit=do_something)
```

## Binary Search Tree

```python
from forest.BinaryTree import BinarySearchTree

tree = BinarySearchTree(10, 'b')
tree[15] = 'k'
tree[17] = 'm'

# search
tree[15]

# removal
del tree[15]
```

## N-ary Tree


```python
from forest.NaryTree import NaryTree

tree = NaryTree(key='1')
branch1 = tree.add_child(key='1.1')
branch2 = tree.add_child(key='1.2')
branch11 = branch1.add_child(key='1.1.1')

def do_something(node):
    print node

tree.traversal(visit=do_something)
```
