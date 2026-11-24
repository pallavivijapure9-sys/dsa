
queue1 = []
queue2 = []

def enqueue(q):
    element = int(input("Enter element: "))
    q.append(element)
    print("Element inserted successfully")

def dequeue(q):
    if not q:
        print("Queue Underflow")
    else:
        print("Deleted element:", q.pop(0))

def display(q):
    if not q:
        print("Queue is Empty")
    else:
        print("Queue elements:", q)

def reverse_queue(q):
    if not q:
        print("Queue is Empty")
    else:
        stack = []

        while q:
            stack.append(q.pop(0))

        while stack:
            q.append(stack.pop())

        print("Queue reversed successfully")

def merge_queues():
    merged = queue1 + queue2
    print("Merged Queue:", merged)

def identical_queues():
    if queue1 == queue2:
        print("Both queues are Identical")
    else:
        print("Queues are NOT Identical")

while True:
    print("\n--- LINEAR QUEUE MENU ---")
    print("1. Enqueue in Queue 1")
    print("2. Dequeue from Queue 1")
    print("3. Display Queue 1")
    print("4. Reverse Queue using Stack")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Enqueue in Queue 2")
    print("8. Display Queue 2")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue(queue1)

    elif choice == 2:
        dequeue(queue1)

    elif choice == 3:
        display(queue1)

    elif choice == 4:
        reverse_queue(queue1)

    elif choice == 5:
        merge_queues()

    elif choice == 6:
        identical_queues()

    elif choice == 7:
        enqueue(queue2)

    elif choice == 8:
        display(queue2)

    elif choice == 9:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")