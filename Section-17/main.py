class Car:
    def __init__(self, plateNumber, make, model, year):
        """Initialize the attributes of the car."""
        self.plateId= plateNumber
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value for odometer
        self.km=0

    def describe_car(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.plateId} {self.year} {self.make} {self.model} {self.km} km"

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't increment by a negative amount!")

car_1 = Car("ABC123", "Toyota", "Camry", 2020)
print(car_1.describe_car()) 