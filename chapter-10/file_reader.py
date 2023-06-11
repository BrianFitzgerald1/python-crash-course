from pathlib import Path


path = Path('text_files/pi_digits.txt')
# path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
# contents = contents.rstrip()
# print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)
