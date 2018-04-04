# Lists are O(n) when inserting to the left (I.E.: FIFO)
# Use a deque object instead, which is O(1) at the ends

from collections import deque

class MyQueue(object):
    def __init__(self):
        self.queue = deque()

    def peek(self):
        return self.queue[-1]

    def pop(self):
        self.queue.pop()

    def put(self, value):
        self.queue.appendleft(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
