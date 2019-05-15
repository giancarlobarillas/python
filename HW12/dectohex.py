# This function taks in a value
# It then has a dictionary of the corresponding values in hex
# While the value is less than 16 it will run until it breaks the
# value down to the lowest base 16 value
def decimalToHex(value):
    hex = []
    conversions = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    while value > 16:
        result = int(value / 16)
        remainder = value % 16
        value = result
        convertedValue = conversions[remainder]
        hex.append(convertedValue)
        if result < 16:
            hex.append(conversions[result])
    return hex


# This is the another version of how to do it with recursion
def decimalToHexrecursvie(value):
    hex = []
    conversions = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    result = int(value / 16)
    print(result)
    if result < 16:
        hex.append(conversions[result])
        print("ending: " + conversions[result])
    else:
        remainder = value % 16
        value = result
        convertedValue = conversions[remainder]
        print("recursive: " + convertedValue)
        decimalToHexrecursvie(value)


# Had to reverse the order in order to properly display
def reverseDisplay(value):
    if (len(value)) == 1:
        return value
    else:
        return reverseDisplay(value[1:]) + [value[0]]


def main():
    print("".join(reverseDisplay(decimalToHex(921))))
    # decimalToHexrecursvie(921)


main()
