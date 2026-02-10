import csv

class BudgetItem():
    TYPE_LIST = ("LIVING", "FOOD", "TRAVEL", "SAVINGS", "LEISURE", "OTHER")
    
    def __init__(self, name, type, amount, description=""):
        self.name = name
        self.type = type
        self.amount = amount
        self.description = description
    
    @property
    def name(self):
        return self._name
    @property
    def type(self):
        return self._type
    @property
    def amount(self):
        return self._amount
    @property
    def description(self):
        return self._description
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.isalpha():
            self._name = value
        else:
            self._name = "n/a"
    @type.setter
    def type(self, value):
        if isinstance(value, str) and value.upper() in self.TYPE_LIST:
            self._type = value.title()
        elif not hasattr(self, 'type'):
            raise ValueError("Invalid type")
    @amount.setter
    def amount(self, value):
        if isinstance(value, str) and value.isdigit():
            self._amount = float(value)
        elif isinstance(value, float) or isinstance(value, int):
            self._amount = float(value)
        elif not hasattr(self, 'amount'):
            raise ValueError("Invalid amount")
    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self._description = value
        elif not hasattr(self, 'description'):
            self._description = ""
    
    def read_from_csv(self, file):
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))