class Jar:
    def __init__(self, capacity=12):
        # If capacity is not a non-negative int, __init__ raises a ValueError.
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError('Invalid Capacity')

        # Initialize the cookie jar with the given capacity.
        # Use '_capacity' to ensure that the capacity function isn't called
        self._capacity = capacity

        # Initially, the number of cookies in the jar is equal to 0 because nothing has been deposited or withdrawn.
        # Use '_size' to ensure that the size function is not called
        self._size = 0

    # __str__ should return a str with n '🍪', where n is the number of cookies in the cookie jar.
    def __str__(self):
        return self.size * '🍪'

    # deposit should add n cookies to the cookie jar
    def deposit(self, n):
        # If adding n cookies to the jar would exceed the jar’s capacity, deposit raises a ValueError.
        if self.size + n > self.capacity:
            raise ValueError(f'Jar cannot fit {n} more cookies')

        self._size += n

    # withdraw should remove n cookies from the cookie jar
    def withdraw(self, n):
        # If there aren’t at least n cookies in the jar when withdraw is called, withdraw raises a ValueError.
        if not self.size >= n:
            raise ValueError('Not enough cookies in jar')

        self._size -= n

    # capacity should return the cookie jar’s capacity
    @property
    def capacity(self):
        return self._capacity

    # size should return the number of cookies actually in the cookie jar
    @property
    def size(self):
        return self._size
