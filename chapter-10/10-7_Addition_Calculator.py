"""10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number."""

"""10-5. Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called 'guest_book.txt'. Make sure each entry appears on a new line in the
file."""


from pathlib import Path
path = Path('chapter-10/text_files/guest_book.txt')

names = ''
while True:
    prompt = "Please enter your name: \n"
    prompt += "(You may submit 'done' when you are finished.)\n"
    name = input(prompt)
    if name != 'done':
        names += f"{name}\n"
    elif name == 'done':
        break

path.write_text(names)
