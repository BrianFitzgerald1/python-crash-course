"""10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly."""

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
