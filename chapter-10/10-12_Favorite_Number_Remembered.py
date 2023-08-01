from pathlib import Path
import json

path = Path('user_favorite_number.json')

if path.exists():
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"I remember your favorite number! It's {fav_number}! ")

else:
    fav_number = input("Tell me your favorite number and I'll remember it. ")
    contents = json.dumps(fav_number)
    path.write_text(contents)

    print(
        f"Your number is {fav_number}. I'll remember that the next time we meet.")
