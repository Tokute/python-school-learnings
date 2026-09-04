class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        head = self.head

        while head is not None:
            print(head.data + " -> ", end="")
            head = head.next

    def insert_data(self):
        new_data = input("\nInput new data: ")
        new_node = Node(new_data)

        current = self.head
        if self.head is None:
            self.head = new_node
            return

        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_data(self):
        to_remove = input("Input data to remove: ")

        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.data == to_remove:
            self.head = self.head.next
            return

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data == to_remove:
                previous.next = current.next
                return

            previous = current
            current = current.next

    print("Data not found.")

if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        print()
        print("Pick an option:")
        print("[1] Insert Data")
        print("[2] Remove Data")
        print("[3] Print List")
        print("[6] Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError as ve:
            print("A value error has occured.")
            choice = -99

        match (choice):
            case 1:
                linked_list.insert_data()
            case 2:
                linked_list.remove_data()
            case 3:
                linked_list.print_list()
            case 6:
                print("Exiting program.")
                break
            case -99:
                continue
            case _:
                print("Error Invalid Choice.")
