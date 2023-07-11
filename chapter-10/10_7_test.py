def get_input_1(input_1):
    """Get a number from the user and verify it is an integer."""
    input_1 = input("Enter an integer: ")
    try:
        number_1 = int(input_1)
    except ValueError:
        print(f"{input_1} is not an integer.")


try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)

except ValueError:
    print("Sorry, I really needed a number.")

else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
