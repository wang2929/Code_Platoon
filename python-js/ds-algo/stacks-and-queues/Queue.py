####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise
import unittest

class TiffQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.insert(0, item)
    
    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        item = self.queue[-1]
        self.queue = self.queue[:-1]
        return item
    
    def peek(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return True if self.size() == 0 else False
    
    def join(self):
        return ''.join(self.queue)
    
    def __str__(self):
        return str(self.queue)
    
    def reverseString(self, strng):
        my_queue = TiffQueue()
        for char in strng:
            my_queue.enqueue(char)
        return my_queue.join()

class TestQueue(unittest.TestCase):
    def test_hello(self):
        queue = TiffQueue()
        word = "hello"
        self.assertEqual(queue.reverseString(word), ''.join(reversed(word)))
        
    def test_with_space(self):
        queue = TiffQueue()
        word = "race car"
        self.assertEqual(queue.reverseString(word), ''.join(reversed(word)))
        
    def test_with_punctuation(self):
        queue = TiffQueue()
        word = "what's upp"
        self.assertEqual(queue.reverseString(word), ''.join(reversed(word)))

    if __name__ == '__main__':
        unittest.main()
