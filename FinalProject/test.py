class Parent(object):
    def __init__(self):
        self.foobar = ["Hello"]


class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        self.foobar.append("world")


def main():
    first = Parent()
    print(first.foobar)
    second = Child()
    print(second.foobar)


main()
