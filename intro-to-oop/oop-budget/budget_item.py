from enum import Enum

class ItemType(Enum):
    # Living, Food, Travel, Savings, and Leisure
    "LIVING" = 1
    "FOOD" = 2
    "TRAVEL" = 3
    "SAVINGS" = 4
    "LEISURE" = 5

class BudgetItem():
    def __init__(self, name, description, type, deposit, withdraw):
        self.name = name
        self.description = description
        self.type = type
        self.deposit = deposit
        self.withdraw = withdraw
    
    @property
    def name(self):
        return self._name
    @property
    def description(self):
        return self._description
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            self._name = "n/a"
    