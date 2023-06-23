"""10-4. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called 'guest.txt'."""

from pathlib import Path

contents = input("Please enter your name: ")

path = Path('chapter-10/text_files/guest.txt')
path.write_text(contents)
