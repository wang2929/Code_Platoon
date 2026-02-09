class User():
    def __init__(self, income, name="anon"):
        self.name = name
        self.income = income
    
    @property
    def income(self):
        return self._income
    @income.setter
    def income(self, value):
        if isinstance(value, str) and value.isdigit():
            self._income = value
        elif isinstance(value, int) and value >= 0:
            self._income = value
        else:
            print("Invalid income")
    