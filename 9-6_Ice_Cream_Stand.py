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
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Display whether the restaurant is open or closed."""
        print(f"{self.restaurant_name} is currently open!")


class IceCreamStand(Restaurant):
    """Another type of restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize atributes of the parent class.
        Then initlaize attributes specific to an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self):
        """Create an empty list called flavors.
        Add any number of ice cream flavors using input()."""
        prompt = "\nWhat flavor should be added to the menu?"
        prompt += "\nYou can type 'done' when you are done making your suggestion(s): "
        flavor = ""
        while flavor != 'done':
            flavor = input(prompt)

            if flavor != 'done':
                self.flavors.append(flavor)
                new_flavor = self.flavors[-1]
                print(f"\n{new_flavor.title()} has been added to the menu.")
            else:
                break

    def display_flavors(self):
        """Display the list of available flavors."""
        print("\nThe following flavors are available to order.")
        for flavor in self.flavors:
            print(flavor)


restaurant = IceCreamStand("Chip's", 'dessert foods')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.add_flavors()
restaurant.display_flavors()
