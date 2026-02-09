from sum_pairs import sum_pairs
import unittest

# write your specs here!
'''
sum_pairs([1,2,3,4,5], 9) # [[4,5]]
sum_pairs([1,2,3,4,5], 7) # [[2,5], [3,4]]
sum_pairs([3, 1, 5, 8, 2], 27) # 'unable to find pairs'
'''

class TestSumPair(unittest.TestCase):
    def test_sum_pairs_exists_1(self):
        self.assertEqual(sum_pairs([1,2,3,4,5], 9),[[4, 5]])

    def test_sum_pairs_exists_2(self):
        self.assertEqual(sum_pairs([1,2,3,4,5], 7), [[2,5], [3,4]])
        
    def test_sum_pairs_dne(self):
        self.assertEqual(sum_pairs([3,1,5,8,2], 27), [])
        
if __name__ == "__main__":
    unittest.main()