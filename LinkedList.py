class LinkedList:

    def __init__(self):
        self.head = None
        
    def print_all(self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()

    def add(self, item):
        self.count = 0
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        if self.head == None:
            self.head = new_node
            self.count += 1  
    
    def remove_from_tail(self): 
        prev = None
        curr = self.head
        while curr.get_next() != None:
            prev = curr
            curr = curr.get_next()
            prev.set_next(None)
