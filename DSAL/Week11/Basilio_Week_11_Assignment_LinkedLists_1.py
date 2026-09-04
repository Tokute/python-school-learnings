# Ned Markus S. Basilio | CS-201

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def move_next(self):
        if self.head.next != "NULL":
            self.head = self.head.next
        else:
            print("Already at the end")

    def move_prev(self):
        if self.head.prev != "NULL":
            self.head = self.head.prev
        else:
            print("Already at the beginning")

    def current_node(self):
        if self.head == None:
            print("Empty Node")
            return

        current = self.head
        next = self.head.next
        previous = self.head.prev

        print("=" * 20)
        print("Current Node:", current.data)
        print("Memory Address:", hex(id(current.data)))
        print("Previous:", previous.data if previous != "NULL" else "NULL")
        print("Next:", next.data if next != "NULL" else "NULL")
        print("=" * 20)

if __name__ == "__main__":
    dbl = DoublyLinkedList()

    node_a = Node("A")
    node_n = Node("N")
    node_g = Node("G")
    node_e = Node("E")
    node_l = Node("L")

    dbl.head = node_a

    node_a.prev = "NULL"    # TAIL
    node_a.next = node_n
    
    node_n.prev = node_a
    node_n.next = node_g

    node_g.prev = node_n
    node_g.next = node_e

    node_e.prev = node_g
    node_e.next = node_l
    
    node_l.prev = node_e
    node_l.next = "NULL"

    # PROGRAM LOOP:

    while True:
        print("\n[1] Move Next")
        print("[2] Move Previous")
        print("[3] Current Node")
        print("[4] Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError as ve:
            print("Value Error has occured. Enter numbers only.")
            continue

        print()

        match (choice):
            case 1:
                dbl.move_next()
            case 2:
                dbl.move_prev()
            case 3:
                dbl.current_node()
            case 4:
                print("Terminating Program...")
                break
