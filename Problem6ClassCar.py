# Daniel Lopez
# 8/18/23
# Create car instances with different attributes and methods for accessing and printing their information

class Car:
    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type  # Attribute
        self.manufacturer = manufacturer  # Attribute
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_color(self):
        return self.color
    
    def get_car_type(self):  # Method
        return self.car_type
    
    def get_manufacturer(self):  # Method
        return self.manufacturer
    
    def fullspecs(self):
        return f"{self.manufacturer} {self.model} {str(self.year)} {self.color} {self.car_type}"  # Modified method

car1 = Car("Sports", 2012, "Blue", "Convertible", "Ferrari")
car2 = Car("Sedan", 2020, "Black", "Sedan", "Toyota")

print(car1.get_color())
print(car1.get_model())
print(car1.get_car_type())  # Print the car type
print(car1.get_manufacturer())  # Print the manufacturer
print(car1.fullspecs())  # Print full specifications

print(car2.get_color())
print(car2.get_model())
print(car2.get_car_type())  # Print the car type
print(car2.get_manufacturer())  # Print the manufacturer
print(car2.fullspecs())  # Print full specifications
