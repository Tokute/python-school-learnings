class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head

        while current:
            print("=" * 50)
            print("Node Data:", current.data)
            print("Node Memory Address:", hex(id(current)))
            current = current.next
        print("=" * 50)

    def add_data_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

if __name__ == "__main__":
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    linked_list = LinkedList()

    for day in days:
        linked_list.add_data_end(day)

    linked_list.print_list()