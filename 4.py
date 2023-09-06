while True:
    # Ask the user to input a 4-digit positive integer or 'q' to quit
    number = input("Enter a 4-digit positive integer or 'q' to quit: ")

    # Check if the user wants to quit
    if number.lower() == 'q':
        break

    # Check if the number has 4 digits
    if len(number) == 4 and number.isdigit():
        number = int(number)
        digit_1 = number // 1000
        digit_2 = (number // 100) % 10
        digit_3 = (number // 10) % 10
        digit_4 = number % 10

        if digit_1 % digit_4 == 0:
            print(f"The first digit ({digit_1}) is a multiple of the fourth digit ({digit_4}).")
        else:
            print(f"The first digit ({digit_1}) is not a multiple of the fourth digit ({digit_4}).")

        sum_of_digits = digit_2 + digit_3
        print(f"The sum of the second and third digits is: {sum_of_digits}")
    else:
        print("The number entered is not a 4-digit positive integer.")
