class Jar:
    def __init__(self, capacity=12, size= 0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n <= (self.capacity - self.size):
            self.size += n
        else:
            raise ValueError("many QTY")

    def withdraw(self, n):
        if n <= self.size:
            self.size -= n
        else:
            raise ValueError("few QTY")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) <= 0:
            raise ValueError("Error")
        else:
            self._capacity = capacity

    @size.setter
    def size(self, size):
        if int(size) < 0:
            raise ValueError("Error")
        else:
            self._size = size

def main():
    cookie = Jar(11)
    cookie.deposit(10)
    cookie.withdraw(5)
    print(cookie.deposit)
    print(cookie.withdraw)
    print(cookie)



if __name__ == "__main__":
    main()
