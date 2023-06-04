"""9-8. Privileges: Write a separate Privileges class. The class should have 
one attribute, privileges, that stores a list of strings as described in 
Exercise 9-7. Move the 'show_privileges()' method to this class. Make a 
'Privileges' instance as an attribute in the 'Admin' class. Create a new 
instance of 'Admin' and use your method to show its privileges."""

"""9-7. Admin: An administrator is a special kind of user. Write a class
called 'Admin' that inherits from the 'User' class you wrote in Exercise 9-3.
or Exercise 9-5. Add an attribute, privileges, that stores a list of strings
like 'can add post', 'can delete post', 'can ban user', and so on. Write a
method called 'show_privleges()' that lists the administrator's set of
privileges. Create and instance of 'Admin', and call your method."""


class User:
    # Attempt to model a user on a website.

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        """Return a description of the user."""
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} and works in {self.location.title()} as a/an {self.occupation}.")

    def greet_user(self):
        """Greet the given user with a personalized message."""
        print(
            f"Hello there {self.first_name.title()}!. I'm glad you are here with us today.\n")


class Admin(User):
    """Creates a type of User with extended privileges."""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to the Admin user type."""
        super().__init__(first_name, last_name, age, location, occupation)


class Privileges:
    # Create a separate privileges class.
    def __init__(self, privileges):
        """Initialize the Privileges class."""
        # self.privileges = privileges
        self.privileges = []

    def add_privileges(self):
        """Adds privileges to a list."""
        self.privileges.append('can add post')
        self.privileges.append('can delete post')
        self.privileges.append('can ban user')

    def show_privleges(self):
        """Display the privileges held by an 'Admin' user type."""
        # print(
        #    f"\n{self.first_name.title()} {self.last_name.title()} has the following privileges.")
        # self.privileges = ['can add post', 'can delete post', 'can ban user']
        for privilege in self.privileges:
            print(privilege)


# user_1 = Admin('tommy', 'timot', '19', 'costa rica', 'painter')
"""Create an admin privileges instance of the 'Privileges' class."""
admin_privileges = Privileges('my_privileges')

"""Call methods from the 'Admin' class, user_1."""
# user_1.describe_user()
# user_1.show_privleges()

"""Call 'show_privileges' method from the 'Privileges' class, admin_privileges."""
admin_privileges.add_privileges()
admin_privileges.show_privleges()
