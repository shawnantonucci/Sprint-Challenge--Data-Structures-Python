class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item

        if self.current + 1 > self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        start = 0
        end = len(self.storage) - 1

        while start <= end:
            middle = start + (end - start) % 2

            if self.storage[middle] == None:
                end = middle - 1
            elif self.storage[middle] is not None:
                start = middle + 1

        return self.storage[: end + 1]


      # if self.storage[self.current] is None:
      #     self.storage[self.current] = self.storage[self.current - 1]
      # return self.storage[self.current:] + self.storage[:self.current]

