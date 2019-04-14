import sys
import string
import argparse

parser=argparse.ArgumentParser(
    prog='checkDigitCalc.py',
    description='''Script for getting the check digits on the swiss id card and passport''')
parser.add_argument('authority number', metavar='n', type=str, nargs=1,
                    help='authority number, it usually starts with a letter and ends with 8-9 numbers')
parser.add_argument('date of birth', metavar='b', type=int, nargs=1,
                    help='date of birth')
parser.add_argument('date of expiry', metavar='e', type=int, nargs=1,
                    help='date of expiry')
parser.add_argument('sex', metavar='s', type=str, nargs=1,
                    help='sex')
parser.add_argument('type of document', metavar='t', type=str, nargs=1,
                    help='id (id) card oder passport (pass)')
args=parser.parse_args()

id_number = sys.argv[1]
birth = sys.argv[2]
expiry = sys.argv[3]
sex = sys.argv[4].upper()
type = sys.argv[5]

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

    count = 0
    for number in numbers:
        product = number * (mulit_list[count%3])
        product_list.append(product)
        count += 1

    return str(sum(product_list)%10)

if type == "id":
    print("IDCHE" + id_number + "<" + getCheckDigit(id_number) + "<<<<<<<<<<<<<<<")
    print(birth + getCheckDigit(birth) + sex + expiry + getCheckDigit(expiry) + "CHE<<<<<<<<<<<" + getCheckDigit(birth + getCheckDigit(birth) + expiry + getCheckDigit(expiry)))
    print("MUSTERMANN<<MAX<<<<<<<<<<<<<<<")

elif type == "pass":
    print("PMCHEMUSTERMANN<<MAX<<<<<<<<<<<<<<<<<<")
    print(id_number + "<" + getCheckDigit(id_number) + "CHE" + birth + getCheckDigit(birth) + sex + expiry + getCheckDigit(expiry) + "<<<<<<<" + getCheckDigit(id_number + "0" + getCheckDigit(id_number) + birth + getCheckDigit(birth) + expiry + getCheckDigit(expiry)))
                                                                                                                                                #add "0" after id_number because we need the mulit_list to skip one ("<" in passport is used for checksum)
else:
    print("please enter a valid document type \n" +
    "   id card --> id\n"+
    "   passport --> pass")
