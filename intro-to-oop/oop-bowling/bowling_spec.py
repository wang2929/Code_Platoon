import unittest
from classes.game import Game
from classes.player import Player
from classes.frame import Frame

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    # Your tests here. Game, Player, and Frame class
    def test_frame_valid_score_open(self):
        new_frame = Frame(*[2, 3])
        self.assertIsInstance(new_frame, Frame)
        self.assertFalse(new_frame.strike)
        self.assertFalse(new_frame.spare)
    
    def test_frame_valid_score_spare(self):
        new_frame = Frame(*[7, 3])
        self.assertIsInstance(new_frame, Frame)
        self.assertFalse(new_frame.strike)
        self.assertTrue(new_frame.spare)
        
    def test_frame_valid_score_strike(self):
        new_frame = Frame(*[10, 0])
        self.assertIsInstance(new_frame, Frame)
        self.assertTrue(new_frame.strike)
        self.assertFalse(new_frame.spare)
        
    def test_frame_invalid_score(self):
        self.assertRaises(Frame(*[4, 7]))
        self.assertRaises(Frame(*[12, 0]))
        self.assertRaises(Frame(*[3, 7, 4]))
        self.assertRaises(Frame(*[-2, 5]))
    
    def test_frame_invalid_score_tenth(self):
        self.assertRaises(Frame(*[2, 3, 2], tenth=True))
        self.assertRaises(Frame(*[3, 7]))

if __name__ == '__main__':
    unittest.main()