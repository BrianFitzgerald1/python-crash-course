"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the restaurant class you
wrote in Exercise 9-1 or 9-4. Either version of the class will work; just pick
the one you like better. Add an attribute called flavors that stores a list of
ice cream flavors. Write a method that displays these flavors. Create an
instance of IceCreamStand, and call this method."""


class Restaurant:
    # Attempt to model a restaurant.

    def __init__(self, restaurant_name, cuisine_type):
        """Initilize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display the name of the restaurant and describes the type of
        cuisine it serves."""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Display whether the restaurant is open or closed."""
        print(f"{self.restaurant_name.title()} is currently open!")


class IceCreamStand(Restaurant):
    """Another type of restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize atributes of the parent class.
        Then initlaize attributes specific to an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    # def temporary_print_flavors(self):
        """Temporary method used to test whether the flavors attribute is created and assigned an empty list."""
        # print(self.flavors)

    def add_flavors(self):
        """Create an empty list called flavors.
        Add any number of ice cream flavors using input()."""
        # flavors = []
        flavor = input("\nWhat flavor should be added to the menu? ")
        self.flavors.append(flavor)
        new_flavor = self.flavors[-1]
        print(f"\n{new_flavor.title()} has been added to the menu.")

    def display_flavors(self):
        """Display the list of available flavors."""
        print("\nThe following list of flavors are available to order.")
        print(self.flavors)


restaurant = IceCreamStand("chip's", 'dessert foods')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# restaurant.temporary_print_flavors()
restaurant.add_flavors()
restaurant.display_flavors()

# restaurant.describe_restaurant()
# restaurant.open_restaurant()
