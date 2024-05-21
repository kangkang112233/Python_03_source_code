import concurrent.futures
import time


# Function to be executed in multiple threads
def worker(n):
    print(f"Worker {n} started")
    time.sleep(2)
    print(f"Worker {n} finished")
    return f"Result from worker {n}"


# Using ThreadPoolExecutor to run tasks concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks
    futures = [executor.submit(worker, i) for i in range(5)]

    # Get results as they complete
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

# Using ThreadPoolExecutor with map
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(worker, range(5))
    for result in results:
        print(result)
