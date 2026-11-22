import time
from functools import wraps

def format_duration(seconds: float):
    minutes, rem_seconds = divmod(seconds, 60)
    hours, rem_minutes = divmod(int(minutes), 60)
    return f"{hours:02d}h {rem_minutes:02d}m {rem_seconds:.3f}s"

def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time

            hours, remainder = divmod(execution_time, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(
                f"Function '{func.__name__}' executed in "
                f"{int(hours)}h {int(minutes)}m {seconds:.3f}s"
            )

    return wrapper

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

@measure_execution_time
def wait_seconds(seconds: int):
    print(f"Waiting for {seconds} seconds...")
    time.sleep(seconds)


for i in range(10):
    wait_seconds(i)

format_duration_seconds(120)