import unittest
from searches import binary_search_sorted_words

class TestingBinarySearch(unittest.TestCase):
    
    def test_1(self):
        sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
        target = 'orange'
        idx, step = binary_search_sorted_words(sorted_word_list, target)
        self.assertEqual(idx, sorted_word_list.index(target))
        print(f"test_1 took {step} steps")
    
    def test_2(self):
        sorted_word_list =  ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
        target = 'banana'
        idx, step = binary_search_sorted_words(sorted_word_list, target)
        self.assertEqual(idx, sorted_word_list.index(target))
        print(f"test_2 took {step} steps")
    
    def test_3(self):
        sorted_word_list =  ['apple', 'avocado', 'banana', 'cherry', 'cranberry', 'durian', 'grape', 'guava', 'mandarin', 'orange', 'persimmon', 'quince', 'strawberry']
        target = 'strawberry'
        idx, step = binary_search_sorted_words(sorted_word_list, target)
        self.assertEqual(idx, sorted_word_list.index(target))
        print(f"test_3 took {step} steps")
    
    def test_3(self):
        sorted_word_list =  ['apple', 'avocado', 'banana', 'cherry', 'cranberry', 'durian', 'grape', 'guava', 'mandarin', 'orange', 'persimmon', 'quince', 'strawberry']
        target = 'strawberry'
        idx, step = binary_search_sorted_words(sorted_word_list, target)
        self.assertEqual(idx, sorted_word_list.index(target))
        print(f"test_4 took {step} steps")
    
    def test_4(self):
        sorted_word_list =  ['apple', 'avocado', 'banana', 'cherry', 'cranberry', 'durian', 'grape', 'guava', 'mandarin', 'orange', 'persimmon', 'quince', 'strawberry']
        target = 'mandarin'
        idx, step = binary_search_sorted_words(sorted_word_list, target)
        self.assertEqual(idx, sorted_word_list.index(target))
        print(f"test_5 took {step} steps for list of length {len(sorted_word_list)}")
    
    def test_5(self):
        sorted_word_list =  ['apple', 'avocado', 'banana', 'cherry', 'cranberry', 'durian', 'grape', 'guava', 'lemon', 'lime', 'lychee', 'mandarin', 'mango', 'orange', 'persimmon', 'pomegranate', 'quince', 'strawberry', 'watermelon']
        target = 'lemon'
        idx, step = binary_search_sorted_words(sorted_word_list, target)
        self.assertEqual(idx, sorted_word_list.index(target))
        print(f"test_5 took {step} steps for list of length {len(sorted_word_list)}")
        
if __name__ == '__main__':
    unittest.main()