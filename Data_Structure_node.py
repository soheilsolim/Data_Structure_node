class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_first(self, d):
        a = Node(d)
        a.next = self.head
        self.head = a

    def add_last(self, d):
        a = Node(d)
        if self.head is None:
            self.head = a
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = a
        
    def add_after(self, d, x):
        if self.head is None:
            return
        temp = self.head
        while temp.data != x:
            if temp.next is None:
                return
            temp = temp.next
        a = Node(d)
        a.next = temp.next
        temp.next = a
        
    def del_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def del_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        
    def del_after(self, x):
        if self.head is None:
            return
        temp = self.head
        while temp.data != x:
            if temp.next is None:
                return
            temp = temp.next
        if temp.next:   
            temp.next = temp.next.next

    def delete(self, x):
        if self.head is None:
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        if self.head.next is None:
            return
        temp = self.head
        while temp.next and temp.next.data == x:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_first(10)
    ll.add_first(20)
    ll.add_last(30)
    ll.add_after(25, 20)
    print("Linked List after additions:")
    ll.display()
    
    ll.del_first()
    print("Linked List after deleting first element:")
    ll.display()
    
    ll.del_last()
    print("Linked List after deleting last element:")
    ll.display()
    
    ll.del_after(20)
    print("Linked List after deleting element after 20:")
    ll.display()
    
    ll.delete(25)
    print("Linked List after deleting element 25:")
    ll.display()
