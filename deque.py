# Deque: A deque.
# Your implementation should pass the tests in test_deque.py.

# Name: Brook Hamilton
# Collaborators:
# Time spent:

# Note: If you're having trouble installing llist, use pyllist instead
#from pyllist import sllist

from llist import dllist

class Deque:
    def __init__(self, items = 0):
        self.items = items
        self.data = dllist()

    def size(self):
        return self.items
    
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def enqueue_left(self, item):
        self.items += 1
        return self.data.appendleft(item)
        
    def enqueue_right(self, item):
        self.items += 1
        return self.data.append(item)
    
    def dequeue_left(self):
        if self.size() == 0:
            raise ValueError("Deque empty")
        else:
            self.items -= 1
            return self.data.popleft()
    
    def dequeue_right(self):
        if self.size() == 0:
            raise ValueError("Deque empty")
        else:
            self.items -= 1
            return self.data.pop()