#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: December 6, 2023
# This program rounds your number to the desired decimal places


def round_decimal(dec_num, dec_num_value_float, num_places):
    # multiply dec_num by 10^num_places, and add 0.5
    dec_num[0] = (dec_num_value_float * 10**num_places) + 0.5

    # convert dec_num to an int
    dec_num[0] = int(dec_num[0])

    # divide dec_num by 10^num_places
    dec_num[0] = dec_num[0] / (10**num_places)


def main():
    # let dec_num be a list
    dec_num = []

    # get decimal number
    dec_num_value_str = input("Enter your decimal number:")

    # append the value to the dec_num list
    dec_num.append(dec_num_value_str)

    # get the desired number of places to be rounded to
    num_places_str = input(
        "How many decimal places do you want your answer rounded to:"
    )

    # if dec_num_value is a float then...
    if dec_num_value_str.replace(".", "").isnumeric():
        # convert dec_num_value to a float
        dec_num_value_float = float(dec_num_value_str)

        # append dec_num_value as a float to dec_num list
        dec_num.append(dec_num_value_float)

        try:
            # convert num_places to an it
            num_places_int = int(num_places_str)

            # call the round decimal function
            round_decimal(dec_num, dec_num_value_float, num_places_int)

            # display the rounded decimal
            print(dec_num[0])
        except:
            # if num_places cannot become an int, tell the user to enter one
            print("{} is not a valid integer.".format(num_places_str))
    else:
        # if dec_num cannot become a number, tell the user to enter one
        print("{} is not a valid decimal number".format(dec_num_value_str))


if __name__ == "__main__":
    main()
