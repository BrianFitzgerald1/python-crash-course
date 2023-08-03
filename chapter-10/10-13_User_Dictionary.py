"""10-13_User_Dictionary: The 'remember_me.py' example only stores one piece of information, the username. Expand this example by asking for two more pieces of information about the user, then store all the information you collect ina dictonary. Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). Print a summary showing exactly what your program remembers about the user."""

from pathlib import Path
import json

path = Path('user_info.json')

user_dict = {}
contents = json.dumps(user_dict)
path.write_text(contents)


def get_user_info():
    username = input("What is your name? ")
    user_age = input("How old are you? ")
    color = input("What is your favorite color? ")

    user_info = {'username': username, 'user age': user_age, 'color': color, }

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


get_user_age()
