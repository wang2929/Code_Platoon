from classes.frame import Frame
        
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.frames:list[Frame] = []
        self.waiting_adjustment = False
    
    @property
    def name(self):
        return self._name.title()
    @name.setter
    def name(self, value):
        self._name = str(value)[:4].upper()
        
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if type(value) == str:
            try:
                value = int(value)
            except:
                raise ValueError("Unable to parse score - cannot read a numerical value.")
        if type(value) == int and 0 <= value <= 300:
            self._score = value
        else:
            raise ValueError("Unable to update score due to invalid score value")
    
    @property
    def number_of_frames(self):
        return len(self.frames)
    
    # for adding a frame
    def add_new_frame(self, *scores):
        try:
            if len(self.frames) == 9:
                new_frame = Frame(*scores, tenth=True)
            else:
                new_frame = Frame(*scores)
        except:
            print("Unable to add this frame - invalid scores")
            return
        self.frames.append(new_frame)
        self.adjust_for_spare_strike()
        if new_frame.spare or new_frame.strike:
            self.waiting_adjustment = True
        else:
            self.calculate_total_score()
        
    # Change the score of the previous frame based on the new frame
    def adjust_for_spare_strike(self):
        # if the previous frame is a spare, add the first roll to the spare
        if len(self.frames) > 1:
            previous_frame = self.frames[-2]
            new_frame = self.frames[-1]
            if previous_frame.spare:
                previous_frame.add_adjustments(new_frame.scores[:1])
            elif previous_frame.strike:
                previous_frame.add_adjustments(new_frame.scores[:2])
    
    # calculate total score
    def calculate_total_score(self):
        self.waiting_adjustment = False
        self.score = 0
        for frame in self.frames:
            self.score += frame.adjusted_score
    
    def __contains__(self, value):
        if str(value) == self.name:
            return True
        return False
    
    # To print the player's game so far
    def __str__(self):
        nm, sc, fr = 4, 3, 3
        padded_name = self.name.ljust(nm)
        padded_score = str(self.score).center(sc)
        padded_adjustment = '-'.center(sc)
        padded_empty = ' ' * fr
        padded_waiting = ' ' * (fr * 3 - 2)
        top_line = f"{padded_name}"
        bottom_line = ' ' * nm
    
        # for player scores
        for i in range(10):
            if i < len(self.frames):
                top_line += str(self.frames[i])
                bottom_line += f"|{padded_adjustment}|"
            else:
                top_line += f"|{padded_empty}|{padded_empty}|"
                bottom_line += f"|{padded_waiting}|"
        if self.waiting_adjustment:
            top_line += f"{padded_adjustment}|"
        else:
            top_line += f"{padded_score}|"
        return top_line + "\n" + bottom_line
    
        