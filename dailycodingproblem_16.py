class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LogRecord(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def record(self, order_id):
        order = Node(order_id)
        if (not self.head):
            self.head = order
            self.tail = order
        else:
            if (self.head == self.tail):
                self.head.next = order
            self.tail.next = order
            order.prev = self.tail
            self.tail = order
        self.length += 1
        return

    def get_last(self, i): # 1 is last, 2-n etc.
        if (i > self.length):
            print("Exceed length of log records")
            exit(1)
        currNode = self.tail;
        i -= 1
        while(i > 0):
            currNode = currNode.prev
            i -= 1
        return currNode


print('INIT')

logRec = LogRecord()
for i in range(10):
    logRec.record(i)

print("Get last elem: ", logRec.get_last(1).value)
print("Get 2nd last elem: ", logRec.get_last(2).value)
print("Get 5th last elem: ", logRec.get_last(5).value)
print("Get first elem: ", logRec.get_last(10).value)
