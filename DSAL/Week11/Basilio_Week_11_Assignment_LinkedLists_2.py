# Ned Markus S. Basilio | CS-201

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def move_next(self):
        if self.last is None:
            print("List is Empty.")
            return

        self.last = self.last.next

        print("=" * 40)
        print("Current Node:", self.last.data)
        print("Memory Address:", hex(id(self.last.data)))
        print("=" * 40)

if __name__ == "__main__":

    cll = CircularLinkedList()

    node_a = Node("A")
    node_n = Node("N")
    node_g = Node("G")
    node_e = Node("E")
    node_l = Node("L")

    cll.last = node_a

    node_a.next = node_n
    node_n.next = node_g
    node_g.next = node_e
    node_e.next = node_l

    node_l.next = cll.last

    while True:
        print("[1] Move Next")
        print("[2] Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError as ve:
            print("ValueError occurred, input only numbers.")
            choice = -99

        match (choice):
            case 1:
                cll.move_next()
            case 2:
                print("Terminating Program...")
                break
            case _:
                print("Invalid Choice. Enter numbers within 1-2.")

        