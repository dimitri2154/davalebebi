import threading
from queue import Queue

def process_number(queue):
    while True:
        number = queue.get()
        print(f"Thread: {threading.current_thread().name}, Number: {number}, Even: {number % 2 == 0}")
        queue.task_done()

def main():
    number_queue = Queue()

    threads = []
    for i in range(3):
        thread = threading.Thread(target=process_number, args=(number_queue,))
        thread.start()
        threads.append(thread)

    for number in range(1, 11):
        number_queue.put(number)

    number_queue.join()

    for _ in range(3):
        number_queue.put(None)

    for thread in threads:
        thread.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()