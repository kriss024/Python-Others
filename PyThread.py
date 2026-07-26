import threading
import time

def print_time(thread_name: str, delay: float) -> None:
    """Prints the current time at specified intervals."""
    for count in range(5):
        time.sleep(delay)
        print(f"{thread_name}: {time.ctime(time.time())}")

def main() -> None:
    # 1. Initialize thread objects
    t1 = threading.Thread(target=print_time, args=("Thread-1", 2.0))
    t2 = threading.Thread(target=print_time, args=("Thread-2", 4.0))

    try:
        # 2. Start execution
        t1.start()
        t2.start()
    except Exception as e:
        print(f"Error: unable to start thread - {e}")
        return

    # 3. Wait for threads to complete (Replaces the CPU-burning `while 1: pass`)
    t1.join()
    t2.join()
    
    print("All threads completed successfully.")

if __name__ == "__main__":
    main()
