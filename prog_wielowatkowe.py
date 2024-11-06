import threading
import time
import random

random.seed(12345)

# Shared variable
shared_data = 0

n_range = 30

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

# Lock for synchronizing access to the shared variable
data_lock = threading.Lock()

# Writer thread function
def writer(name: str):
    global shared_data
    for i in range(n_range):
        with data_lock:  # Lock access to shared_data
            shared_data += 1
            print(f"{name} updated shared_data to {shared_data}")

        time.sleep(random.random())

# Reader thread function
def reader(name: str):
    for i in range(n_range):
        with data_lock:  # Lock access to shared_data
            print(f"\t{name} read shared_data as {shared_data}")

        time.sleep(random.random())

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

print("Starting the program.")

# Create threads
writer_thread = threading.Thread(target=writer, args=("Writer",))
reader_thread = threading.Thread(target=reader, args=("Reader",))

# Start threads
writer_thread.start()
reader_thread.start()

# Wait for both threads to complete
writer_thread.join()
reader_thread.join()

print("Program finished.")
