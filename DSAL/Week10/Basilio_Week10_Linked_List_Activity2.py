class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp_list = []
        current = self.head
        while current is not None:
            temp_list.append(current.data)
            current = current.next

        to_print = " -> ".join(temp_list)
        print(to_print)

    def get_size(self):
        current = self.head

        size = 0
        while current is not None:
            size += 1
            current = current.next

        return size

    def add_data_start(self):
        new_data = input("Enter new data to add: ")
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def add_data_end(self):
        new_data = input("Enter new data to add: ")
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def add_data_middle(self):
        size = self.get_size()

        if size == 0:
            print("List is empty.")
            new_data = input("Enter new data: ")
            self.head = Node(new_data)
            return

        target_node = (size - 1) // 2

        if target_node == 0:
            new_data = input("Enter new data: ")
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        previous = None

        for _ in range(target_node):
            previous = current
            current = current.next

        new_data = input("Enter new data: ")
        new_node = Node(new_data)

        previous.next = new_node
        new_node.next = current

    def remove_node(self):
        to_remove = input("Enter data to remove: ")

        head = self.head
        if head is not None:
            if (head.data == to_remove):
                self.head = head.next
                head = None
                return

        while head is not None:
            if head.data == to_remove:
                break
            previous = head
            head = head.next

        if head == None:
            return

        previous.next = head.next
        head = None


if __name__ == "__main__":
    node_1 = Node("bird")
    node_2 = Node("cat")
    node_3 = Node("dog")
    node_4 = Node("elephant")
    node_5 = Node("snake")

    linked_list = LinkedList()

    linked_list.head = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    while True:
        print("Linked List Values:")
        linked_list.print_linked_list()
        print()

        print("=== Options ===")
        print("[1] Add item at the beginning of the list")
        print("[2] Add item at the end of the list")
        print("[3] Add item at the middle of the list")
        print("[4] Remove an item from the list")
        print("[5] Exit")

        try:
            choice = int(input("Choice: "))
        except Exception as e:
            print("Error. Please input only numerals")
        print()

        match choice:
            case 1:
                linked_list.add_data_start()
            case 2:
                linked_list.add_data_end()
            case 3:
                linked_list.add_data_middle()
            case 4:
                linked_list.remove_node()
            case 5:
                print("Program has ended.")
                break
            case _:
                print("Error Invalid Choice. Input only 1-5.")

