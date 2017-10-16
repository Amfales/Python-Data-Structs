from collections import deque
class Queue():
    def __init__(self,start=None):
        if start is None:
            start = []

        self._length = len(start)
        self._items = deque(start)

    def __len__(self):
        return self._length

    def __str__(self):
        return "Queue: [%s]" % (' '.join(map(str,self._items)))

    def enqueue(self,item):
        self._items.append(item)
        self._length += 1

    def dequeue(self):
        if self._length == 0:
            raise RuntimeError("Empty Queue")
        self._length -= 1
        return self._items.popleft()


def main():
    print("Testing Queue class...")
    q = Queue()
    print("Queue is initially empty")
    print(q)

    print("Adding values 1,2")
    q.enqueue(1)
    q.enqueue(2)
    print(q)

    print("Dequeueing one value")
    item = q.dequeue()
    print("Item dequeued: %s" % (item))
    print(q)


if __name__ == '__main__':
    main()
