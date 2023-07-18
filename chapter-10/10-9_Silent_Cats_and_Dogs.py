"""Modify your except block in Exercise 10-8 to fail silently if either file is missing."""

from pathlib import Path

path_1 = Path('text_files/cats.txt')
path_2 = Path('text_files/dogs.txt')

try:
    contents_1 = path_1.read_text()
    print(contents_1)

except FileNotFoundError:
    print("Sorry, but this file can't be found in this directory.\nTry switching to another directory.")

try:
    contents_2 = path_2.read_text()
    print(contents_2)

except FileNotFoundError:
    print("Sorry, but this file can't be found in this directory.\nTry switching to another directory.")
