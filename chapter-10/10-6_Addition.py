"""10-6. Addition: One common problem when programming for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you'll get a ValueError. Write a program that prompts for
two numbers. Add them together an print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test
your program by entering two numbers and then by entering some text instead of
a number."""

print("Give me any two numbers and I will add them together for you.\n")

while True:
    input_1 = input("Enter the first number: ")
    print(f"The value you entered is {input_1}.\n")
    if type(input_1) != int:
        print(f"{input_1} is not an interger.")
        input_1 = input("Please enter an interger value.")
    elif type(input_1) == int:
        break

input_2 = input("Please enter the second number: ")
print(f"The value you entered is {input_2}.\n")

number_1 = int(input_1)

number_2 = int(input_2)

result = number_1 + number_2
print(f"Adding the two numbers produces {result}.")
