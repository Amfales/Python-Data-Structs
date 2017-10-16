import heapq as hq
_REMOVED = '<removed>'
class PriorityQueue():
    def __init__(self,minHeap=True):
        start = []
        self._length = len(start)
        self._gen = self._uniqueIdGen()
        self._isMinHeap = minHeap
        self._items = []
        self._lookup = {}

    def __bool__(self):
        return self._length > 0
    def __len__(self):
        return self._length

    def __str__(self):
        return "Priority Queue: [%s]" % (' '.join(map(str,self._items)))

    def insert(self,prior,item):
        if (item in self._lookup):
            self._deleteItem(item)
        tempItem = [prior if self._isMinHeap else -1*prior
                    ,next(self._gen),item]
        self._lookup[tempItem[-1]] = tempItem
        hq.heappush(self._items,tempItem)
        self._length += 1

    def deleteMin(self):
        while self:
            item = hq.heappop(self._items)
            if item[-1] is not _REMOVED:
                del self._lookup[item[-1]]
                self._length -= 1
                return item
        raise KeyError("Empty Priority Queue")

    def _deleteItem(self,item):
        actItem = self._lookup.pop(item)
        actItem[-1] = _REMOVED
        
    
    

    def _uniqueIdGen(self):
        curId = 0
        while True:
            yield curId
            curId += 1
    


def main():
    print("Priority Queue is in the form [priority,order,item]")
    print("Testing Priority Queue class...")
    pq = PriorityQueue()
    print("Priority Queue is initially empty")
    print(pq)

    print("Adding values 1,2 with priorities 2,1")
    pq.insert(2,1)
    pq.insert(1,2)
    print(pq)

    print("Changing priority of 2 to 10")
    pq.insert(10,2)
    print(pq)

    print("Deleting smallest value")
    item = pq.deleteMin()
    print("Item deleted: %s" % (str(item)))
    print(pq)


if __name__ == '__main__':
    main()
