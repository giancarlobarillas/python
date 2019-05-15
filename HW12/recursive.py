# This application displays a list of an array in reverse order
# It start with a reverseDisplay function that takes in a value and then
# return the reverse
def reverseDisplay(value):
    if (len(value)) == 1:
        return value
    else:
        return reverseDisplay(value[1:]) + [value[0]]


def main():
    list = [1, 2, 3, 4, 5]
    print(reverseDisplay(list))


main()
