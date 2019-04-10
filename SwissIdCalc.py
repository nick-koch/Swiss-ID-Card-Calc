import sys
import string
import argparse

parser=argparse.ArgumentParser(
    prog='swissIdCalc.py',
    description='''Script for getting the check digits on the swiss id card''')
parser.add_argument('authority number', metavar='n', type=str, nargs=1,
                    help='it\'s the string on the front and the back of the id card. starts usually with a letter and ends with 8-9 numbers')
parser.add_argument('date of birth', metavar='b', type=int, nargs=1,
                    help='date of birth is written on bottom the front in bold letters')
parser.add_argument('date of expiry', metavar='e', type=int, nargs=1,
                    help='date of expiry is on the back of the id')
args=parser.parse_args()


id_number = sys.argv[1]
birth = sys.argv[2]
expiry = sys.argv[3]


def getCheckDigit(str_numbers):
    numbers = []

    for str_char in str_numbers:
        if str_char.isalpha():
            int_char = string.ascii_lowercase.index(str_char.lower()) + 10
        else:
            int_char = int(str_char)

        numbers.append(int_char)

    mulit_list = [7, 3, 1]
    product_list = []

    counter = 0
    for number in numbers:
        product_list.append(number * mulit_list[counter])
        counter = counter + 1
        if counter == 3:
            counter = 0

    product_list_last_digit = []

    for prod in product_list:
        product_list_last_digit.append(int(str(prod)[-1]))

    sum_of_last_digits = sum(product_list_last_digit)

    return str(sum_of_last_digits)[-1]


print("IDCHE" + id_number + "<" + getCheckDigit(id_number))
print(birth + getCheckDigit(birth) + "M/F" + expiry + getCheckDigit(expiry) + "CHE<<<<<<<" + getCheckDigit(birth + getCheckDigit(birth) + expiry + getCheckDigit(expiry)))
