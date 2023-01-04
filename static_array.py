

class StaticArrayException(Exception):
    """
    Custom exception for Static Array class.
    """
    pass


class StaticArray:
    """
    Implementation of Static Array Data Structure.
    Implemented methods: get(), set(), length()
    """

    def __init__(self, size: int = 10) -> None:
        """
        Create array of given size.
        Initialize all elements with values of None.
        If requested size is not a positive number,
        raise StaticArray Exception.
        """
        if size < 1:
            raise StaticArrayException('Array size must be a positive integer')

        self._size = size
        self._data = [None] * size

    def __iter__(self) -> None:

        return None

    def __str__(self) -> str:
        """Override string method to provide more readable output."""
        return f"STAT_ARR Size: {self._size} {self._data}"

    def get(self, index: int):
        """
        Return value from given index position.
        Invalid index raises StaticArrayException.
        """
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        return self._data[index]

    def set(self, index: int, value) -> None:
        """
        Store value at given index in the array.
        Invalid index raises StaticArrayException.
        """
        if index < 0 or index >= self.length():
            raise StaticArrayException('Index out of bounds')
        self._data[index] = value

    def __getitem__(self, index: int):
        """Enable bracketed indexing."""
        return self.get(index)

    def __setitem__(self, index: int, value: object) -> None:
        """Enable bracketed indexing."""
        self.set(index, value)

    def length(self) -> int:
        """Return length of the array (number of elements)."""
        return self._size


if __name__ == "__main__":

    # Using the Static Array #

    # Can use either the get/set methods or [] (bracketed indexing)         #
    # Both are public methods; using the [] calls the corresponding get/set #

    # Create a new StaticArray object - is the default size
    arr = StaticArray()

    # These two statements are equivalent
    arr.set(0, 'hello')
    arr[0] = 'hello'

    # These two statements are equivalent
    print(arr.get(0))
    print(arr[0])

    # Print the number of elements stored in the array
    print(arr.length())

    # Create a new StaticArray object to store 5 elements
    arr = StaticArray(5)

    # Set the value of each element equal to its index multiplied by 10
    for index in range(arr.length()):
        arr[index] = index * 10

    # Print the values of all elements in reverse order
    for index in range(arr.length() - 1, -1, -1):
        print(arr[index])
