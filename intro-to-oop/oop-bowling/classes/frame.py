class Frame:
    def __init__(self, *scores, tenth=False):
        self.tenth_frame = tenth
        self.scores = scores
        self.adjustments = []
    
    @property
    def scores(self):
        return self._scores
    @scores.setter
    def scores(self, value):
        if len(value) != 2 and len(value) != 3:
            raise Exception(f"Need the correct number of scores. Received {len(value)} scores, expected 2 or 3.")
        self.scores_are_valid(value)    # function raises error if invalid
        # logic for bowling game
        two_rolls_sum = int(value[0]) + int(value[1])
        if self.tenth_frame:
            if len(value) == 3:
                if two_rolls_sum != 10:
                    raise Exception(f"Too many scores received. Only spares or strikes on the first two rolls can roll a third time.")
                self._scores = value
        elif len(value) == 2:
            if two_rolls_sum < 0 or two_rolls_sum > 10:
                raise Exception(f"Sum of scores is not valid. Score {value} adds up to {two_rolls_sum}, expecting between 0 to 10")
            self._scores = value
        else:
            raise Exception("Received 3 scores on a frame before the 10th frame")
        
    @property
    def spare(self):
        if self.scores[0] < 10 and self.scores[0] + self.scores[1] == 10:
            return True
        return False
    
    @property
    def strike(self):
        if self.scores[0] == 10:
            return True
        return False
    
    @property
    def raw_score(self):
        return sum(self.scores)
    
    # -1 as placeholder to wait for valid score
    @property
    def adjusted_score(self):
        if self.tenth_frame:    # tenth frame needs no adjustments
            return self.raw_score
        # all other frames should be adjusted for spares and strikes
        if self.strike:
            if len(self.adjustments) == 2:
                return self.raw_score + sum(self.adjustments)
            return -1
        elif self.spare:
            if len(self.adjustments) == 1:
                return self.raw_score + self.adjustments[0]
            return -1
        else:
            return self.raw_score
    
    def add_adjustments(self, value:list):
        if self.strike and len(value) != 2:
            raise Exception(f"Strike adjustment needs 2 scores, received {len(value)}")
        elif self.spare and len(value) != 1:
            raise Exception(f"Spare adjustment needs 1 score, received {len(value)}")
        for val in value:
            Frame.roll_is_valid(val) # raises error if invalid
            self.adjustments.append(val)

    @staticmethod
    def scores_are_valid(scores):
        for roll in scores:
            Frame.roll_is_valid(roll)
    
    @staticmethod
    def roll_is_valid(roll):
        if type(roll) == str:
            try:
                roll = int(roll)
            except:
                raise Exception("Unable to parse a numerical score.")
        if type(roll) == int:
            if roll < 0 or roll > 10:
                raise Exception(f"Score of {roll} is not within 0-10.")
        else:
            raise Exception("Unable to interpret score")

    def __str__(self):
        sz = 3
        padded_empty = ' '.center(sz)
        padded_strike = 'X'.center(sz)
        padded_spare = '/'.center(sz)
        padded_first = self.scores[0].center(sz)
        padded_second = self.scores[1].center(sz)
        padded_total_2 = self.adjusted_score.center(sz*3 - 2) if self.adjusted_score >= 0 else '-'.center(sz*3 - 2)
        padded_total_3 = self.adjusted_score.center(sz*4 - 2)
        # 10th frame only has 3 if there was a strike or spare first
        # print X on strikes and / on spares for tenth frame
        if self.tenth_frame:
            if self.scores[0] == 10:    # can have three strikes, strike and spare, strike and open
                padded_third = self.scores[2].center(3)
                # three strikes
                if self.scores[1] == 10 and self.scores[2] == 10:
                    return f"|{padded_strike}|{padded_strike}|{padded_strike}|\n|{padded_total_3}|"
                # strike then spare
                elif self.scores[1] + self.scores[2] == 10:
                    return f"|{padded_strike}|{padded_second}|{padded_spare}|\n|{padded_total_3}|"
                # strike then open
                else:
                    return f"|{padded_strike}|{padded_second}|{padded_third}|\n|{padded_total_3}|"
            elif self.scores[0] + self.scores[1] == 10:    # first two rolls make a spare, plus third roll
                padded_third = self.scores[2].center(3)
                # spare then strike
                if self.scores[2] == 10:
                    return f"|{padded_first}|{padded_spare}|{padded_strike}|\n|{padded_total_3}|"
                # spare then open
                else:
                    return f"|{padded_first}|{padded_spare}|{padded_third}|\n|{padded_total_3}|"
            else:
                # open on the tenth is like a regular open
                return f"|{padded_first}|{padded_second}|\n|{padded_total_2}|"
        elif self.spare:
            return f"|{padded_first}|{padded_spare}|\n|{padded_total_2}|"
        elif self.strike:
            return f"|{padded_strike}|{padded_empty}|\n|{padded_total_2}|"
        else:
            return f"|{padded_first}|{padded_second}|\n|{padded_total_2}|"