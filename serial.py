"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Creates a new instance of SerialGenerator, indicated by a number"""
        self.start = start
        self.current = start
        # self.start = self.next = start

    def __repr__(self) -> str:
        return str(self.current)
        # return f"<SerialGenerator start={self.start} next={self.next}"

    def generate(self):
        """Increments the number representing the SerialGenerator instance by 1"""
        value = self.current
        self.current += 1
        return value
        # self.next += 1
        # return self.next -1

    def reset(self):
        """Returns the number representing the SerialGenerator instance to its original number"""
        self.current = self.start
        # self.next = self.start

serial = SerialGenerator(start=100) # should return 100

print(serial)

serial.generate() # should return 101

print(serial)

serial.generate() # should return 102

print(serial)

serial.reset() # should return 100

print(serial)