class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width

    def __lt__(self, other):
        return int(self.get_area()) < other

    def __le__(self, other):
        return int(self.get_area()) <= other

    def __eq__(self, other):
        return int(self.get_area()) == other

    def __ne__(self, other):
        return int(self.get_area()) != other

    def __gt__(self, other):
        return int(self.get_area()) > other

    def __ge__(self, other):
        return int(self.get_area()) >= other




# Test Code 1
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 == a2)
# print(a1 != a3)

# Test code 2
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 != a2)
# print(a1 >= a3)

# Test code 3
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)