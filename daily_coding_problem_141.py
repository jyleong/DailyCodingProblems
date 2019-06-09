'''
Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
'''

class Stack:
    def __init__(self):
        self.list = []
        self.idx = [None, None, None]
        self.sizes = [0, 0, 0]

    def get_list(self):
        return self.list

    def pop(self, stack_number):
        if self.idx[stack_number] is None:
            raise Exception("No items in this stack")

        item = self.list.pop(self.idx[stack_number])
        self.sizes[stack_number] -= 1
        if stack_number == 0:
            # do for 1 and 2
            if self.idx[1] is not None:
                self.idx[1] -=1
            if self.idx[2] is not None:
                self.idx[2] -= 1

        if stack_number == 1:
            # do for 2
            if self.idx[2] is not None:
                self.idx[2] -= 1

        return item

    def push(self, item, stack_number):
        if self.idx[stack_number] is not None:
            self.list.insert(self.idx[stack_number], item)
            self.sizes[stack_number] += 1
            if stack_number == 0:
                # do for 1 and 2
                if self.idx[1] is not None:
                    self.idx[1] += 1
                if self.idx[2] is not None:
                    self.idx[2] += 1
            if stack_number == 1:
                if self.idx[2] is not None:
                    self.idx[2] += 1
        else: # is None make new
            if stack_number == 0:
                self.list.insert(0, item)
                self.sizes[0] += 1
                self.idx[0] = 0
                if self.idx[1] is not None:
                    self.idx[1] += 1
                if self.idx[2] is not None:
                    self.idx[2] += 1
            if stack_number == 1:
                offset = self.sizes[0]
                self.list.insert(offset, item)
                self.idx[1] = offset
                self.sizes[1] += 1
                if self.idx[2] is not None:
                    self.idx[2] += 1
            if stack_number == 2:
                offset = self.sizes[0] + self.sizes[1]
                self.list.insert(offset, item)
                self.idx[2] = offset
                self.sizes[2] += 1
                

if __name__ == "__main__":
    
    stack_3 = Stack()

    stack_3.push(2, 0)

    stack_3.push(3, 1)

    assert stack_3.get_list() == [2, 3]

    stack_3.push(4, 0)

    assert stack_3.get_list() == [4, 2, 3]

    stack_3.push(9, 0)


    assert stack_3.get_list() == [9, 4, 2, 3]

    stack_3.push(5, 1)


    assert stack_3.get_list() == [9, 4, 2, 5, 3]

    stack_3.push(3, 2)

    stack_3.push(1, 1)

    assert stack_3.get_list() == [9, 4, 2, 1, 5, 3, 3]

    assert stack_3.pop(1) == 1
    assert stack_3.get_list() == [9, 4, 2, 5, 3, 3]
    assert stack_3.pop(1) == 5
    assert stack_3.get_list() == [9, 4, 2, 3, 3]
    assert stack_3.pop(1) == 3
    assert stack_3.get_list() == [9, 4, 2, 3]

    stack_3.push(8, 2)

    assert stack_3.get_list() == [9, 4, 2, 8, 3]

    stack_3.push(7, 1)

    assert stack_3.get_list() == [9, 4, 2, 7, 8, 3]