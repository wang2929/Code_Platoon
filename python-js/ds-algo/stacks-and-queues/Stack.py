####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise
import unittest

class TiffStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        ret = self.stack[-1]
        self.stack = self.stack[:-1]
        return ret
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return True if self.size() == 0 else False
    def __str__(self):
        return str(self.stack)

    def reverseString(self, s):
        my_stack = TiffStack()
        for char in s:
            my_stack.push(char)
        ret = []
        while (not my_stack.is_empty()):
            ret.append(my_stack.pop())
        return ''.join(ret)

class TestStack(unittest.TestCase):
    def test_hello(self):
        stack = TiffStack()
        word = "hello"
        self.assertEqual(stack.reverseString(word), ''.join(reversed(word)))
        
    def test_with_space(self):
        stack = TiffStack()
        word = "race car"
        self.assertEqual(stack.reverseString(word), ''.join(reversed(word)))
        
    def test_with_punctuation(self):
        stack = TiffStack()
        word = "what's upp"
        self.assertEqual(stack.reverseString(word), ''.join(reversed(word)))

    if __name__ == '__main__':
        unittest.main()