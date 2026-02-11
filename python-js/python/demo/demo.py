class Mother:
    def __init__(self):
        self.first_name = "Sandra"
        self.last_name = "Wilensky"


class Father:
    def __init__(self):
        self.first_name = "Harris"
        self.last_name = "Cohen"


class Child(Mother, Father):
    def __init__(self):
        # try swapping the order of these initializing statements
        # Mother first - mother's last name
        # Father first - father's last name
        Father.__init__(self)
        Mother.__init__(self)
        
        self.first_name = "Benjamin"

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")


ben = Child()
ben.print_full_name()