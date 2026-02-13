from classes.frame import Frame
        
class Player:
    BAD_NAME_COUNT = 0
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.frames:list[Frame] = []
    
    @property
    def name(self):
        return self._name.upper()
    @name.setter
    def name(self, value):
        try:
            self._name = str(value)
        except:
            self._name = f"NEW PLAYER {Player.BAD_NAME_COUNT}"
            Player.BAD_NAME_COUNT += 1
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if type(value) == str:
            try:
                value = int(value)
            except:
                print("Unable to parse score - no updates to score")
                return
        if type(value) == int and 0 <= value <= 300:
            self._score = value
        else:
            print("Unable to update score - invalid score value")
            return
        
    # Change the score of the previous frame based on the new frame
    def adjust_for_spare_strike(self):
        # if the previous frame is a spare, add the first roll to the spare
        previous_frame = self.frames[-2]
        new_frame = self.frames[-1]
        if previous_frame.spare:
            previous_frame.adjusted_score = previous_frame.raw_score + new_frame.first
        elif previous_frame.strike:
            previous_frame.adjusted_score = previous_frame.raw_score + new_frame.first + new_frame.second
    
    # calculate total score
    def calculate_total_score(self):
        self.adjust_for_spare_strike()
        for frame in self.frames:
            if frame.adjusted_score >= 0:
                self.score += frame.adjusted_score
    
    # for adding a frame
    def add_new_frame(self, *scores):
        if len(self.frames) == 9:
            new_frame = Frame(scores, tenth=True)
        else:
            new_frame = Frame(scores)
        self.frames.append(new_frame)
        self.calculate_total_score()
    
    # To print the player's game so far
    def __str__(self):
        ret_str = f"{self.name}|"
        for i in range(10):
            if i < len(self.frames):
                ret_str += str(self.frames[i])
            ret_str += "|   |   |"
        ret_str += f"|{self.score}"
        return ret_str
    
        