from DHeap import DHeap


class PriorityQueue:

    def __init__(self, isMaxHeap=False):
        self.pq = DHeap(isMaxHeap)

    def add(self, e):
        self.pq.add(e)

    def poll(self):
        if (self.pq.size() == 0):
            return None
        else:
            return self.pq.remove()

    def size(self):
        return self.pq.size()
