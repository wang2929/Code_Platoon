# Practicing with class attributes

class CarManager:
    all_car = {}
    total_cars = 0
    
    def __init__(self, make="n/a", model="n/a", year="n/a", mileage="n/a"):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services = []
        CarManager.total_cars += 1
        self.id = str(CarManager.total_cars)
        CarManager.all_car[self.id] = self
    
    @property
    def make(self):
        return self._make
    @make.setter
    def make(self, value):
        if value == "": self._make = "n/a"
        else: self._make = value
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, value):
        if value == "": self._model = "n/a"
        else: self._model = value
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        if value == "": self._year = "n/a"
        else: self._year = value
    @property
    def mileage(self):
        return self._mileage
    @mileage.setter
    def mileage(self, value):
        if value == "": self._mileage = "n/a"
        else: self._mileage = value
    @property
    def services(self):
        return self._services
    @services.setter
    def services(self, value):
        self._services = value

    def add_service(self, value):
        self.services.append(value)
    
    def update_mileage(self, value):
        self.mileage = value
    
    def __str__(self):
        return f"ID: {self.id}, Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}, Services: {self.services}"