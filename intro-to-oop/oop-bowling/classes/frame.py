class Frame:
    def __init__(self, *scores, tenth=False):
        self.first, self.second, self.third = scores
        self.tenth_frame = tenth
        self.raw_score = self.first + self.second + self.third
        # spare and strike are flags for adjusting score; applies when not the 10th frame)
        self.spare = True if (self.first + self.second) == 10 else False
        self.strike = True if self.first == 10 else False
        self.adjusted_score = -1 if self.spare or self.strike else self.raw_score
    
    @property
    def first(self):
        return self._first
    @first.setter
    def first(self, value):
        if self.roll_is_valid(value):
            self._first = value
            
    @property
    def second(self):
        return self._second
    @second.setter
    def second(self, value):
        if self.roll_is_valid(value):
            self._second = value
            
    @property
    def third(self):
        return self._third
    @third.setter
    def third(self, value):
        if self.roll_is_valid(value):
            self._third = value

    @staticmethod
    def roll_is_valid(roll):
        if type(roll) == str:
            try:
                roll = int(roll)
            except:
                print("Unable to parse score")
        if type(roll) == int and 0 <= roll <= 10:
            return True
        else:
            print("Unable to interpret score")
        
    @staticmethod
    def raw_score_is_valid(*args):
        if len(args) != 3:
            return False
        for score in args:
            if score < 0 or score > 10:
                return False
        return True

    def __str__(self):
        if self.tenth_frame:
            # 10th frame only has 3 if there was a strike or spare first
            # print X on strikes and / on spares for tenth frame
            if self.first == 10:    # can have three strikes, strike and spare, strike and open
                if self.second == 10 and self.third == 10:
                    print("| X | X | X")
                elif self.second + self.third == 10:
                    print(f"| X | {self.second} | / |")
                else:
                    print(f"| X | {self.second} | {self.third} |")
            elif self.first + self.second == 10:    # cannot have a strike on the second without strike on the first
                if self.third == 10:
                    print(f"| {self.first} | / | X |")
                else:
                    print(f"| {self.first} | / | {self.third} |")
            else:
                print(f"| {self.first} | {self.second} |")
        elif self.spare:
            print(f"| {self.first} | / |")
        elif self.strike:
            print("| X |   |")
        else:
            print(f"| {self.first} | {self.second} |")