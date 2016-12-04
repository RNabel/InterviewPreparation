class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
        self.first_out_of_date = False
        self.second_out_of_date = False

    def peek(self):
        if self.first_out_of_date:
            self.first = self.second[::-1]
            self.first_out_of_date = False

        return self.first[0]

    def pop(self):
        if self.second_out_of_date:
            self.second = self.first[::-1]
            self.second_out_of_date = False

        self.first_out_of_date = True
        self.second.pop()

    def put(self, value):
        if self.first_out_of_date:
            self.first = self.second[::-1]
            self.first_out_of_date = False

        self.second_out_of_date = True
        self.first.append(value)


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()

