class Stack:

    def __init__(self, items = [], limit = 100):
        pass
        self.items = items
        self.limit = limit

    def isEmpty(self):
        pass
        return len(self.items) == 0

    def push(self, item):
        pass
        if not self.full():
            self.items.append(item)

    def pop(self):
        pass
        if not self.isEmpty():
            # raise Exception("Stack is Empty!")
            item = self.items[-1]
            self.items.pop()
            return item

    def peek(self):
        pass
        if not self.isEmpty():
            # raise Exception("Stack is Empty!")
            return self.items[-1]

    def size(self):
        pass
        return len(self.items)

    def full(self):
        pass
        return self.limit == self.size()

    def search(self, target):
        pass
        distance = -1
        index = self.size()-1
        while index >=0:
            distance +=1
            if target == self.items[index]:
                return distance
            index -=1

        return -1

