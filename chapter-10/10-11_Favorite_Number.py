"""10-11. Favorite Number: Write a program that prompts for the user's favorite number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message 'I know your favorite number! It's ___!'"""

from pathlib import Path
import json

path = Path('user_favorite_number.json')

fav_number = input("Tell me your favorite number and I'll remember it. ")
contents = json.dumps(fav_number)
path.write_text(contents)

print(
    f"Your number is {fav_number}. I'll remember that the next time we meet.")
