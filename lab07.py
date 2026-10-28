# Fill in the two functions and the two classes below (look for the TODO comments).
#
# Parts 1 and 2 must use RECURSION - a function that calls itself on a smaller version
# of the problem. Do NOT use a loop for those two.
#
# Do not rename anything, because the automated tests use these names.


def count_occurrences(target, values):
    # Base case: an empty list contains it 0 times.
    if not values:
        return 0
    
    # Recursive case: 1 (if the first item equals `target`, otherwise 0) plus the
    # count in the rest of the list, values[1:].
    match = 1 if values[0] == target else 0
    return match + count_occurrences(target, values[1:])


def is_sorted(values):
    # Base case: a list of 0 or 1 items is already sorted.
    if len(values) <= 1:
        return True
    
    # Recursive case: the first two items are in order AND the rest is sorted.
    return values[0] <= values[1] and is_sorted(values[1:])


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.width}x{self.height}"


class Square(Rectangle):   # Part 4 - stretch (optional)
    def __init__(self, side):
        # Pass `side` as both the width and height to the parent Rectangle class
        super().__init__(side, side)


def main():
    # Scratch space tests
    print(count_occurrences(2, [1, 2, 2, 3, 2]))   # Expected: 3
    print(is_sorted([1, 2, 3]))                    # Expected: True
    print(is_sorted([1, 3, 2]))                    # Expected: False
    print(Rectangle(3, 4).area())                  # Expected: 12
    print(Square(5))                               # Expected: 5x5


if __name__ == "__main__":
    main()