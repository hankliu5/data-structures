from DHeap import DHeap


class PriorityQueue:
    """Implemented by d-nary heap."""

    def __init__(self, isMaxHeap=False):
        self.pq = DHeap(isMaxHeap)

    def add(self, e):
        """Adds a new element to the heap."""
        self.pq.add(e)

    def poll(self):
        """Removes and returns the top element of the heap.
        If the heap is empty, returns None."""
        if (self.pq.size() == 0):
            return None
        else:
            return self.pq.remove()

    def size(self):
        """Returns the size of the heap."""
        return self.pq.size()
