class Queue(object):
    '''Defines a Queue (en.wikipedia.org/wiki/Queue)'''

    def __init__(self, items=None):
        if items is None:
            self.items = []
        self._queue = self.items
    
    def is_empty(self):
        return len(self._queue) == 0
    
    def enqueue(self, obj):
        self._queue.append(obj)
    
    def dequeue(self):
        return self._queue.pop(0)
    
    def access(self):
        return self._queue[0]


class Stack(object):
    """Defines a Stack (en.wikipedia.org/wiki/stack_(data_structure))"""
    def __init__(self, items=None):
        if items is None:
            self.items = []
        self._stack = self.items
    
    def is_empty(self):
        return len(self._stack) == 0
    
    def push(self, obj):
        self._stack.append(obj)
    
    def pop(self):
        return self._stack.pop(len(self._stack) - 1)
    
    def top(self):
        return self._stack[len(self._stack) - 1]
