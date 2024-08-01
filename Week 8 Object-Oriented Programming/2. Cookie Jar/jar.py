class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n >= 0:
            self.size = self.size + int(n)
            return self.size
        else:
            raise ValueError

    def withdraw(self, n):
        if n >= 0:
            self.size = self.size - int(n)
            return self.size
        else:
            raise ValueError

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size
    @size.setter
    def size(self, size):
        if size  < 0 or size > self.capacity:
            raise ValueError
        self._size = size


jar = Jar()
