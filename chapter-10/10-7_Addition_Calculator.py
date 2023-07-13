"""10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number."""

"""10-6. Addition: One common problem when programming for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you'll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number."""

while number
try:
    number_1 = input("Enter a number: ")
    number_1 = int(number_1)

    number_2 = input("Enter another number: ")
    number_2 = int(number_2)

except ValueError:
    print("Sorry, I really need a number.")

else:
    sum = number_1 + number_2
    print(f"The sum of {number_1} and {number_2} is {sum}.")
