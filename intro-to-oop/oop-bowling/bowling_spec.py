import unittest
from classes.game import Game
from classes.player import Player
from classes.frame import Frame

class TestGame(unittest.TestCase):
    
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
        with self.assertRaises(Exception):
            Frame([4, 7]) # sum too large
            Frame([12, 0]) # roll too large
            Frame([3, 7, 4]) # too many rolls
            Frame([-2, 5]) # roll too small
            Frame([7])  #too few rolls
    
    def test_frame_invalid_score_tenth(self):
        with self.assertRaises(Exception):
            Frame([2, 3, 2], tenth=True) # too many rolls
            Frame([3, 7], tenth=True) # too few rolls w/ spare
            Frame([10], tenth=True) # too few rolls w/ strike 1
            Frame([10, 5], tenth=True) # too few rolls w/ strike 2  
    
    def test_frame_valid_adjustment_strike(self):
        new_frame = Frame(*[10, 0])
        new_frame.add_adjustments([3, 5])
        self.assertEqual(new_frame.adjusted_score, 10 + 3 + 5)
        
    def test_frame_valid_adjustment_spare(self):
        new_frame = Frame(*[3, 7])
        new_frame.add_adjustments([5])
        self.assertEqual(new_frame.adjusted_score, 3 + 7 + 5)
    
    def test_frame_bad_adjustment_strike(self):
        new_frame = Frame(*[10, 0])
        with self.assertRaises(Exception):
            new_frame.add_adjustments(*[3, 5, 2])
            new_frame.add_adjustments(*[2])
    
    def test_frame_bad_adjustment_spare(self):
        new_frame = Frame(*[6, 4])
        with self.assertRaises(Exception):
            new_frame.add_adjustments(*[2, 3])
    
    def test_player_set_name(self):
        self.assertEqual(Player("Steven").name, "Stev")
        self.assertEqual(Player("Joe").name, "Joe")
        self.assertEqual(Player("Anna").name, "Anna")
    
    def test_player_add_open(self):
        new_player = Player("Tiff")
        new_player.add_new_frame(*[3, 2])
        self.assertEqual(new_player.score, 5)
        new_player.add_new_frame(*[5, 3])
        self.assertEqual(new_player.score, 13)
    
    def test_player_add_spares(self):
        new_player = Player("Tiff")
        new_player.add_new_frame(*[5, 5])
        self.assertEqual(new_player.score, 0)
        self.assertTrue(new_player.waiting_adjustment)
        new_player.add_new_frame(*[8, 1])
        self.assertEqual(new_player.score, 27)
        self.assertFalse(new_player.waiting_adjustment)
    
    def test_player_add_strikes(self):
        new_player = Player("Tiff")
        new_player.add_new_frame(*[10, 0])
        self.assertEqual(new_player.score, 0)
        self.assertTrue(new_player.waiting_adjustment)
        new_player.add_new_frame(*[8, 1])
        self.assertEqual(new_player.score, 28)
        self.assertFalse(new_player.waiting_adjustment)
    
    def test_player_add_bad_frame(self):
        new_player = Player("Tiff")
        new_player.add_new_frame(*[4, 7]) # sum too large
        self.assertEqual(new_player.number_of_frames, 0)
        new_player.add_new_frame(*[12, 0]) # roll too large
        self.assertEqual(new_player.number_of_frames, 0)
        new_player.add_new_frame(*[3, 7, 4]) # too many rolls
        self.assertEqual(new_player.number_of_frames, 0)
        new_player.add_new_frame(*[-2, 5]) # roll too small
        self.assertEqual(new_player.number_of_frames, 0)
        new_player.add_new_frame(*[7])  #too few rolls
        self.assertEqual(new_player.number_of_frames, 0)
    
    def test_game_update_player_name(self):
        new_game = Game()
        new_game.update_player_name('1', 'Tiff')
        self.assertTrue('Tiff' in new_game)
        new_game.update_player_name('nobody', 'bud')
        new_game.update_player_name('2', 'Tiff')
    
    def test_game_add_valid_frames(self):
        new_game = Game()
        print(new_game)

if __name__ == '__main__':
    unittest.main()