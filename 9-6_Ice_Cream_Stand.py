"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the restaurant class you
wrote in Exercise 9-1 or 9-4. Either version of the class will work; just pick
the one you like better. Add an attribute called flavors that stores a list of
ice cream flavors. Write a method that displays these flavors. Create an
instance of IceCreamStand, and call this method."""


class Restaurant:
    """Attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initilize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 2

    def describe_restaurant(self):
        """Display the name of the restaurant and describes the type of
        cuisine it serves."""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Display whether the restaurant is open or closed."""
        print(f"{self.restaurant_name.title()} is currently open!")

    def read_number_served(self):
        """Print a statement showing the number of people served so far."""
        print(
            f"This restaurant has served {self.number_served} customers so far.")

    def update_number_served(self, number_served):
        """Set the number of customers served to the given value."""
        self.number_served = number_served

    def increase_number_served(self, number_served):
        """Add a set amount to the number served."""
        self.number_served += number_served


restaurant = Restaurant('big-C', 'turkish food')

restaurant.describe_restaurant()
restaurant.open_restaurant()
# restaurant.number_served = 49
restaurant.read_number_served()
# restaurant.update_number_served(4_011)
# restaurant.read_number_served()
restaurant.increase_number_served(20)

restaurant.read_number_served()
