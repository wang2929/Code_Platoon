from classes.player import Player
from classes.frame import Frame

class Game:
    def __init__(self, num_of_players=4):
        self.players: list[Player] = []
        for i in range(num_of_players):
            self.players.append(Player(i+1))
    
    def print_all_players(self):
        for i in range(len(self.players)):
            print(f"Player {i+1}: {self.players[i]}, {self.players[i].score}")
    
    def update_player_name(self, old_name, new_name):
        if old_name in self.players:
            if new_name not in self.players:
                idx = self.players.index(old_name)
                self.players[idx].name = new_name
            else:
                print(f"Unable to update name - {new_name} is taken!")
        else:
            print(f"Unable to update name - cannot find {old_name}")
    
    def add_frame(self, player_name, *scores):
        if len(scores) == 2:
            scores.append(0)
        if len(scores) != 3:
            print(f"Unable to add frame - Given {len(scores)} rolls, expected 2 or 3")
            return
        if not Frame.raw_score_is_valid(*scores):
            print(f"Unable to add frame - Invalid scores {scores}")
            return            
        idx = self.players.index(player_name)
        self.players[idx].add_new_frame(scores)
        
    def __str__(self):
        ret_str = "--- Bowling ---\n"
        for player in self.players:
            ret_str += str(player) + '\n'
        return ret_str