"""10-6. Addition: One common problem when programming for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you'll get a ValueError. Write a program that prompts for two numbers. Add them together an print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number."""

prompt = "Give me any two numbers and I will add them together for you.\n"
print(prompt)

input_1 = input("Enter the first number: ")
input_2 = input("Please enter the second number: ")


number_1 = int(input_1)
print(f"The value you entered is {input_1}.")

number_2 = int(input_2)

result = number_1 + number_2
print(result)
