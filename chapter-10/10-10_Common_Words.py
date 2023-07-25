from pathlib import Path

path = Path('text_files/skull-face.txt')
contents = path.read_text()

small_contents = contents.lower()

print(small_contents.count('the '))
