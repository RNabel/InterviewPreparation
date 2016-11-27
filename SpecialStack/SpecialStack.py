class SpecialStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.nums = []
        self.mins = []

    def push(self, num):
        self.nums.append(num)
        if len(self.mins):
            self.mins.append(min(self.mins[-1], num))
        else:
            self.mins.append(num)

    def pop(self):
        self.mins.pop()
        return self.nums.pop()

    def is_empty(self):
        return len(self.nums) == 0

    def is_full(self):
        return len(self.nums) == self.max_size

    def get_min(self):
        return self.mins[-1]


if __name__ == '__main__':
    s = SpecialStack(10)
    s.push(10)
    s.push(20)
    s.push(30)
    print s.get_min()
    s.push(5)
    print s.get_min()

