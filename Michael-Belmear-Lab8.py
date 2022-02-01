# -----------------------------------------------------
# CSCI 127, Lab 8                                     |
# March 18, 2021                                      |
# Michael Belmear                                     |
# -----------------------------------------------------

# Your solution goes here. ------------------------------
class Queue:
    def __init__(self, name):
        self.queue_name = name
        self.items = []# start the queue as an empty list

    def enqueue(self, item):
        self.items.insert(0, item)

    def __iadd__(self, item):
        self.items.insert(0, item)
        
        # Fix me: make the += operator work
        return self.items # must return self from __iadd__

    def dequeue(self):
        self.items.pop()
        return self.items

    def is_empty(self):
        # Fix me: Only return true when no presedents are in the queue
        if self.items == []:
            return True
        else:
            return False
        
    def __str__(self):
        str1 = " "
        return "Queue: " + "[FIRST-->" + str1.join(self.items) +"<--LAST]"
    
# Do not change anything below. -------------------------

def main():
    presidents = Queue("Presidents")

    print("\nAdding George W, John A, TJ, Jimmy M, J Monroe")
    presidents.enqueue("Washington")
    presidents.enqueue("Adams")
    presidents.enqueue("Jefferson")
    presidents.enqueue("Madison")
    presidents.enqueue("Monroe")
    print(presidents)

    print("\nDequeue George (First in, first out: FIFO)")
    presidents.dequeue()
    print(presidents)

    print("\nDequeue everybody")
    while not presidents.is_empty():
        print("President dequeued:", presidents.dequeue())
        print(presidents)

    print("\nAdding JQ Adams, Andy J, MVB, B Harrison, Johnny T")
    presidents.enqueue("Adams")
    presidents.enqueue("Jackson")
    presidents.enqueue("Van Buren")
    presidents.enqueue("Tyler")
    print(presidents)

    print("\nAdding Jimmy KP to the back of the line")
    presidents += "Polk" # See: https://www.python-course.eu/python3_magic_methods.php
    print(presidents)

# -----------------------------------------------------

main()
