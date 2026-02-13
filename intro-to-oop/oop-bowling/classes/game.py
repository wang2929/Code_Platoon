from classes.player import Player
from classes.frame import Frame

class Game:
    def __init__(self, num_of_players=4):
        self.players: list[Player] = []
        for i in range(num_of_players):
            new_player = Player(i+1)
            self.players.append(new_player)
    
    def print_all_players(self):
        for i in range(len(self.players)):
            print(f"Player {i+1}: {self.players[i].name}, {self.players[i].score}")
    
    def get_player(self, name):
        for player in self.players:
            if name in player:
                return player
        print(f"Didn't find {name}")
        return -1
    
    def update_player_name(self, old_name, new_name):
        old_name = str(old_name)[:4].title()
        new_name = str(new_name)[:4].title()
        if type(the_player := self.get_player(old_name)) == Player:
            if type(self.get_player(new_name)) == int:
                print(f"Updating name {old_name} to {new_name}")
                the_player.name = new_name
            else:
                print(f"Unable to update name - {new_name} is taken!")
        else:
            print(f"Unable to update name - cannot find {old_name}")
    
    def add_frame(self, player_name, *scores):          
        the_player = self.get_player(player_name)
        the_player.add_new_frame(scores)
        
    def print_to_file(self):
        msg = self.__str__()
        with open('output/game_state.txt', 'w') as f:
            print(msg, file=f)
        
    def __contains__(self, value):
        for player in self.players:
            if player.name == str(value):
                return True
        return False
        
    def __str__(self):
        ret_str = "~~~~~ Let's Go Bowling ~~~~~\n"
        nm, fr = 4, 3
        # for header
        header = ' ' * nm
        for i in range(10):
            header += f"{str(i+1).center(fr*3)}"
        ret_str += header + "\n"
        # now print players
        for player in self.players:
            ret_str += str(player) + '\n'
        return ret_str