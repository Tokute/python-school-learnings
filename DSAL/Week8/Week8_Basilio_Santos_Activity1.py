
# Code By: Ned Markus Basilio and Cryztelle Jhoy Santos  | CS-201

queue_item = []
front = 0
rear = -1
output_file = open("display.txt", "w")
newline = lambda: output_file.write("\n")

def enqueue():
    global rear

    if len(queue_item) < 10:
        item = input("Enter item to enqueue: ")
        queue_item.append(item)
        rear = len(queue_item) - 1
        print(f"+ Enqueued: {item}")
        output_file.write(f"+ Enqueued: {item}\n")
    else:
        print(f"Queue is full. Cannot enqueue.")
        output_file.write(f"! Queue is full. Cannot enqueue.\n")

def dequeue():
    global front
    global rear

    if len(queue_item) > 0:
        item = queue_item.pop(0)

        front = 0 if queue_item else -1
        rear = len(queue_item) - 1 if queue_item else -1

        print(f"- Dequeued: {item}")

        output_file.write(f"- Dequeued: {item}\n")

    else:
        print("Queue is empty. Cannot dequeue.")
        output_file.write(f"! Queue is empty. Cannot dequeue.\n")

output_file.write("Code By: Ned Markus S. Basilio and Cryztelle Jhoy Santos | CS-201\n")
newline()

while True:
    print("==OPTION==")
    print("[1] Enqueue")
    print("[2] Dequeue")
    print("[3] Display")
    print("[4] Exit")
    user_option = int(input("Enter option: "))

    match user_option:
        case 1:
            enqueue()
        case 2:
            dequeue()
        case 3:
            print("Queue contents:")
            output_file.write("Queue contents:\n")
            newline()
            for item in queue_item:
                print(f" - {item}")
                output_file.write(f" - {item}\n")

            newline()
            output_file.write(f"Front index: {front}, Rear index: {rear}\n")
            output_file.write(f"Front item: {queue_item[front] if front != -1 else 'None'}, Rear item: {queue_item[rear] if rear != -1 else 'None'}\n")
            newline()
        case 4:
            print("Exiting...")
            break
        case _:
            print("Invalid option. Please input 1-4.")

output_file.close()