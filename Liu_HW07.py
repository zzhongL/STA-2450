#Assignment HW 07
#Student Name :Zhizhong Liu
#Last Changed Date:10/21/2024

#Exercise 1: Create a Book Class
class Book:
    def __init__(self, title, author, pages, year_published):
        """
        A new Book instance.

        Parameters:
        t   itle (str): The title of the book.
        author (str): The author of the book.
        pages (int): The number of pages in the book.
        year_published (int): The year the book was published.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.year_published = year_published

    def description(self):
        """
        Return a description including the book's title, author, and number of pages.
        """
        return f"'{self.title}' by {self.author}, {self.pages} pages."


# Creating some Book objects
book1 = Book("journey to the west", "Wu chengen", 1000, 1600)
book2 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 309, 1998)
book3 = Book("King Lear", "William Shakespeare", 384, 1608)

# Printing the descriptions
print(book1.description())
print(book2.description())
print(book3.description())

#Exercise 3: Create a Vehicle Class with Subclasses
class Vehicle:
    """A class representing a vehicle with make and model."""
    def __init__(self, make, model):
        """
        A new Vehicle instance.

        Parameters:
        make (str): The make of the vehicle.
        model (str): The model of the vehicle.
        """
        self.make = make
        self.model = model

    def vehicle_type(self):
        """Return a string representing the type of vehicle."""
        return "Vehicle Parents Class"


class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        """
        Truck instance.

        Parameters:
        make (str): The make of the truck.
        model (str): The model of the truck.
        payload_capacity (int): The payload capacity of the truck in kg.
        """
        super().__init__(make, model)
        self.payload_capacity = payload_capacity

    def vehicle_type(self):
        return "Truck"


class Motorcycle(Vehicle):
    def __init__(self, make, model, cc):
        """
        Motorcycle instance.

        Parameters:
        make (str): The make of the motorcycle.
        model (str): The model of the motorcycle.
        cc (int): The engine capacity of the motorcycle in cubic centimeters.
        """
        super().__init__(make, model)
        self.cc = cc

    def vehicle_type(self):
        """Return the type of vehicle."""
        return "Motorcycle"


# Creating objects for Truck and Motorcycle
truck1 = Truck("Tesla", "2024 Tesla Cybertruck", 2500)
motorcycle1 = Motorcycle("FRP", "FRP DB003", 50)

# Calling their methods
print(f"{truck1.vehicle_type()}: {truck1.make} {truck1.model}, Payload Capacity: {truck1.payload_capacity} kg")
print(f"{motorcycle1.vehicle_type()}: {motorcycle1.make} {motorcycle1.model}, Engine Capacity: {motorcycle1.cc} cc")
