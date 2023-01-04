

from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        """
        return self._capacity

    def get_data(self, index) -> object:
        """
        get data from an index
        """
        return self._data[index]

    def set_capacity(self, new_capacity) -> None:
        """
        set new capacity
        """
        self._capacity = new_capacity

    def set_size(self, new_size) -> None:
        """
        Set new size
        """
        self._size = new_size

    def set_data(self, data: object):
        """
        set new array
        """
        self._data = data

    def set_append(self, index: int, value: object):
        """
        sets data to an appended index
        """

        self._data[index] = value

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity for the elements in the dynamic array
        """
        #if new capacity invalid, do nothing
        if new_capacity <= 0 or new_capacity < self.length():
            return

        #resize the array with new capacity
        else:
            data = StaticArray(new_capacity)

            #copy any data in array to new array with new capacity to resize array
            for count in range(self.length()):
                data[count] = self.get_data(count)

            self.set_capacity(new_capacity)
            self.set_data(data)


    def append(self, value: object) -> None:
        """
        Adds new value at end of dynamic array.  If storage is full double array capacity
        """

        #resize array to twice current capacity if array is at max capacity
        if self.get_capacity() == self.length():
            current_capacity = self.get_capacity()
            self.resize(current_capacity * 2)

        #add data to next empty element in the dynamic array
        self.set_append(self.length(), value)
        self.set_size(self.length() + 1)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds new value at specified index in dynamic array
        """

        #resize if array at capacity
        if self.get_capacity() == self.length():
            current_capacity = self.get_capacity()
            self.resize(current_capacity * 2)

        #if index is invalid raise exception
        if index < 0 or index > self.length():
            raise DynamicArrayException()

        #find index to insert element at and then insert at that index
        for count in range(self.length(), index, -1):
            self.set_append(count, self.get_data(count - 1))

        #increase length of data in the array after element added
        self.set_append(index, value)
        new_length = self.length()
        new_length += 1
        self.set_size(new_length)

    def remove_at_index(self, index: int) -> None:
        """
        Remove element at specified index in dynamic array
        """

        #raise exception if index is invalid
        if index < 0 or index > self.length() - 1:
            raise DynamicArrayException()

        #reduce capacity if required
        if self.length() < self.get_capacity() / 4:

            new_capacity = 2 * self.length()

            if new_capacity > 10:
                self.resize(new_capacity)

            if self.length() * 2 < 10 and self.length() != 1:
                self.resize(10)

        #find index to remove and copy rest of array
        for count in range(index, self.length() - 1):
            self.set_append(count, self.get_data(count + 1))

        if self.length() > 0:
            size = self.length() - 1
            self.set_append(size, None)
            new_length = self.length()
            new_length -= 1
            self.set_size(new_length)

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns new DynamicArray that contains requested number of elements from original array
        """

        #raise exception if index is invalid
        if start_index < 0 or start_index > self.length() - 1 or start_index + size > self.length() or size < 0:
            raise DynamicArrayException()

        split_index = start_index + size
        split_arr = DynamicArray()

        #split array at requested index and return split array
        for count in range(start_index, split_index, 1):
            split_arr.append(self.get_data(count))

        return split_arr


    def merge(self, second_da: "DynamicArray") -> None:
        """
        Take array as parameter and append all elements to current array in the same order they are stored
        """

        second_da_length = second_da.length()

        for count in range(second_da_length):
            self.append(second_da[count])


    def map(self, map_func) -> "DynamicArray":
        """
        Returns new dynamic array where value of each element is derived by applying a map_func corresponding to a value
        from original array
        """

        map_array = DynamicArray()

        for count in range(self.length()):

            map_data = map_func(self.get_data(count))
            map_array.append(map_data)

        return map_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        create new dynamic array populated only with elements from filter_func = true from original array
        """

        filter_array = DynamicArray()

        #loop through array and apply filter function to each element and put it in dynamic array
        for count in range(self.length()):
            filter_data = filter_func(self.get_data(count))
            if filter_data is True:
                filter_array.append(self.get_data(count))

        return filter_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Apply reduce_func to all elements in dynamic array and return result
        """

        #if there is no initializer value
        if initializer is None:
            value = self.get_data(0)

            #apply reduce function to each element in array
            for count in range(self.length() - 1):
                next_val = self.get_data(count + 1)
                value = reduce_func(value, next_val)

        #if there is an initializer value, place it beginning of array
        else:
            value = initializer

            #apply reduce function to each element of the array and also use initializer value
            for count in range(self.length()):
                next_val = self.get_data(count)
                value = reduce_func(value, next_val)

        return value


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Return a tuple with a dynamic array of the mode and an integer representing the highest frequency
    """

    mode_count = 0
    mode = DynamicArray()
    max_frequency = 0
    index = 0

    if arr.length() == 1:
        return (arr[0], 1)

    for count in range(arr.length() - 1):
        #count numbers appearing more than once
        if arr.get_data(count) == arr.get_data(count + 1):
            mode_count += 1

        #looks at final element in array
        if arr.get_data(count) != arr.get_data(count + 1) and max_frequency == 0 and count == arr.length() - 2:
            mode.append(arr[count])
            mode.append(arr[count + 1])
            max_frequency = 1
            return (mode, max_frequency)

        #find the highest number of repeated items and return as the mode and the frequency rate
        if mode_count >= max_frequency:
            if mode_count > max_frequency and arr[count] != arr[count + 1]:
                    mode = DynamicArray()
                    max_frequency = mode_count
                    mode.append(arr[count])
                    mode_count = 0

            if mode_count == max_frequency and arr[count] != arr[count + 1]:
                mode.append(arr[count])
                mode_count = 0
                index += 1

            if mode_count == max_frequency and arr[count] == arr[count + 1] and count == arr.length() - 2 and arr[count] != mode.get_data(index):
                mode.append(arr[count])
                index += 1

            if mode_count > max_frequency and arr[count] == arr[count + 1] and count != arr.length():
                mode = DynamicArray()
                max_frequency = mode_count
                mode.append(arr[count])
                mode_count = 0

        #resize mode array if at capacity
        if mode.length() == 4:
            mode.resize(mode.length() * 2)

    max_frequency += 1

    return (mode, max_frequency)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
