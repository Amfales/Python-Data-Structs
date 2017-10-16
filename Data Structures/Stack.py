class Stack():
    def __init__(self,start=None):
        if start is None:
            start = []
        self._length = len(start)
        self._items = start[:]

    def __len__(self):
        return self._length

    def __str__(self):
        return "Stack: [%s]" % (' '.join(map(str,self._items)))

    def push(self,item):
        self._length += 1
        self._items.append(item)

    def pop(self):
        if self._length == 0:
            raise RuntimeError("Empty Stack")
        self._length -= 1
        return self._items.pop()
        


def main():
    print("Testing Stack class...")
    s = Stack()
    print("Stack is initially empty")
    print(s)

    print("Adding values 1,2")
    s.push(1)
    s.push(2)
    print(s)

    print("Popping one value")
    item = s.pop()
    print("Item popped: %s" % (item))
    print(s)


if __name__ == '__main__':
    main()
