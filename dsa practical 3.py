import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    # 1. Add Process (Enqueue)
    def enqueue(self, pid, name, priority):
        if priority < 1 or priority > 4:
            print("Invalid Priority! Enter 1 to 4.")
            return

        heapq.heappush(
            self.queue, (priority, self.counter, pid, name)
        )
        self.counter += 1
        print("Process added successfully!")

    # 2. Execute Process (Dequeue)
    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
        else:
            p = heapq.heappop(self.queue)
            print("\nExecuting Process:")
            print("Process ID:", p[2])
            print("Process Name:", p[3])
            print("Priority:", p[0])

    # 3. View Next Process
    def display_next(self):
        if not self.queue:
            print("No pending processes!")
        else:
            p = self.queue[0]
            print("\nNext Process:")
            print("Process ID:", p[2])
            print("Process Name:", p[3])
            print("Priority:", p[0])

    # 4. Display All Processes
    def display_all(self):
        if not self.queue:
            print("No pending processes!")
        else:
            print("\nAll Pending Processes:")
            for p in sorted(self.queue):
                print("ID:", p[2],
                      "Name:", p[3],
                      "Priority:", p[0])

    # 5. Count Processes
    def count(self):
        print("Total Pending Processes:", len(self.queue))


# Main Program
pq = PriorityQueue()

while True:
    print("\n===== CPU PROCESS SCHEDULING =====")
    print("1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Process ID: "))
        name = input("Enter Process Name: ")
        priority = int(input("Enter Priority (1-4): "))
        pq.enqueue(pid, name, priority)

    elif choice == 2:
        pq.dequeue()

    elif choice == 3:
        pq.display_next()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        pq.count()

    elif choice == 6:
        print("Exiting CPU Scheduler...")
        break

    else:
        print("Invalid Choice! Try Again.")
