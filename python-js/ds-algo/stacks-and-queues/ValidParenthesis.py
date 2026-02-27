from Stack import TiffStack
import unittest

class Solution:
    # with personal stack
    def isValidTiffStack(self, s: str) -> bool:
        left_brackets = ['(', '{', '[']
        matching_brackets = { '(':')', '[':']', '{':'}' }
        stack = TiffStack()
        for br in s:
            if br in left_brackets:
                stack.push(br)
            else:
                try:
                    curr = stack.pop()
                    if matching_brackets[curr] != br:
                        return False
                except:
                    # missing matching left bracket
                    return False
        return True if stack.is_empty() else False
    
    # list implementation
    def isValid(self, s:str) -> bool:
        left_brackets = ['(', '{', '[']
        matching_brackets = { '(':')', '[':']', '{':'}' }
        stack = []
        for br in s:
            if br in left_brackets:
                stack.append(br)
            else:
                try:
                    curr = stack.pop()
                    if matching_brackets[curr] != br:
                        return False
                except:
                    # missing matching left bracket
                    return False
        return True if len(stack) == 0 else False

class TestParenthesis(unittest.TestCase):
        
    def test_basic(self):
        word, soln = "()", Solution()
        self.assertEqual(soln.isValid(word), True)
        
    def test_not_basic(self):
        word, soln = "())", Solution()
        self.assertEqual(soln.isValid(word), False)
        
    def test_single_left(self):
        word, soln = "(", Solution()
        self.assertEqual(soln.isValid(word), False)
        
    def test_single_right(self):
        word, soln = ")", Solution()
        self.assertEqual(soln.isValid(word), False)
    
    def test_nested(self):
        word, soln = "([])", Solution()
        self.assertEqual(soln.isValid(word), True)
    
    def test_nested_mismatch(self):
        word, soln = "([]}", Solution()
        self.assertEqual(soln.isValid(word), False)
    
    if __name__ == '__main__':
        unittest.main()

