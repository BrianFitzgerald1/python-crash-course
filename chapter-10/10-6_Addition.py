"""10-6. Addition: One common problem when programming for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you'll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test
your program by entering two numbers and then by entering some text instead of
a number."""

print("Give me any two numbers and I will add them together for you.\n")

active_1 = True
active_2 = True
input_1 = input("Enter the first number: ")
input_2 = input("Please enter the second number: ")

while active_1 == True:
    try:
        number_1 = int(input_1)
    except ValueError:
        print(f"The value {input_1} is not an integer.")
        input_1 = input("Enter another number: ")
        active_1 = False

while active_2 == True:
    try:
        number_2 = int(input_2)
    except ValueError:
        print(f"\nThe value {input_2} is not an integer.")
        input_2 = input("Enter another number: ")
        active_2 = False

result = number_1 + number_2
print(f"Adding the two numbers produces {result}.")
