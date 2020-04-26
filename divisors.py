which = input("Do you want to convert a number to or from binary? (to/from): ")
global result


def converter():
    den = int(input("Please enter a number to convert to binary: "))
    binary = ""
    while den > 0:
        binary = str(den % 2) + binary
        den = den // 2
    print("Your number in binary is: ", binary)
    print(den)


def decimal():
    binary = input("Please input a binary value: ")
    dec = 0
    for digit in binary:
        dec = dec*2 + int(digit)
    print("Your decimal number is: ", str(dec))


if which == "to":
    converter()
elif which == "from":
    decimal()
