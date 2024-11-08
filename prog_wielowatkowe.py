import threading
import time
import random

random.seed(12345)

# Shared variable - must be a list, because scalars are not mutable!
shared_data = [0]

max_range = 30

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

# Lock for synchronizing access to the shared variable
data_lock = threading.Lock()

# Writer thread function
def writer(max_range: int):
    while shared_data[0] <= max_range:
        with data_lock:  # Lock access to shared_data
            shared_data[0] += 1
            print(f"Writer updated shared_data to {shared_data[0]}")

        time.sleep(random.random())
    else:
        print('Loop done.')

# Reader thread function
def reader(max_range: int):
    while shared_data[0] <= max_range:
        with data_lock:  # Lock access to shared_data
            print(f"\tReader read shared_data as {shared_data[0]}")

        time.sleep(random.random())
    else:
        print('Loop done.')

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

print("Starting the program.")

# Create threads
writer_thread = threading.Thread(target=writer, args=(max_range,))
reader_thread = threading.Thread(target=reader, args=(max_range,))

# Start threads
writer_thread.start()
reader_thread.start()

# Wait for both threads to complete
writer_thread.join()
reader_thread.join()

print("Program finished.")
