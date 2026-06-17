class c_queue:
    """Circular queue implementation. For tracking user login attempts."""
    def __init__(self, size):
        self.head = -1
        self.tail = -1
        self.size = size
        self.data = [None] * (self.size)

    def enqueue(self, data):
        if self.is_full():
            return
        if self.head == -1:
            self.head = 0

        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = data
     
    def dequeue(self):
        if self.is_empty():
            return None
        
        current = self.data[self.head]
        if(self.head == self.tail):
            self.tail = -1
            self.head = -1
        else:
            self.data[self.head] = None
            self.head = (self.head + 1) % self.size
        return current
    
    def show(self):
        print("------------------===Queue===-------------------")
        for i in range(self.size):
            print(f"Index {i}: {self.data[i]}")
        print("-------------------------------------------------")   
    
    def peek(self):
        return self.data[self.head]
    
    def is_empty(self):
        if(self.head == -1):
            return True
        return False
    
    def is_full(self):
        if (self.tail + 1) % self.size == self.head:
            return True
        return False
