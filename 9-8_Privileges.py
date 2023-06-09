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

    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} and works in {self.location.title()} as a/an {self.occupation}.")

    def greet_user(self):
        print(
            f"Hello there {self.first_name.title()}!. I'm glad you are here with us today.\n")


class Privileges:

    def __init__(self, privileges_list=[]):
        self.privileges_list = privileges_list
        self.privileges_list.append('can add post')
        self.privileges_list.append('can delete post')
        self.privileges_list.append('can ban user')

    def show_privleges(self):
        print("This user has a following privileges")
        for privilege in self.privileges_list:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, age, location, occupation):
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges()


user_1 = Admin('tommy', 'timot', '19', 'costa rica', 'painter')

"""Call methods from the 'Admin' class, user_1."""
user_1.describe_user()


user_1.privileges.show_privleges()
