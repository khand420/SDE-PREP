import multiprocessing
import time

def cpu_bound_task():
    start = time.time()
    for _ in range(100000000):
        pass  # some CPU-bound operation
    end = time.time()
    print(f"Process {multiprocessing.current_process().name} finished in {end - start:.2f} seconds")

# Create two processes
process1 = multiprocessing.Process(target=cpu_bound_task, name='Process-1')
process2 = multiprocessing.Process(target=cpu_bound_task, name='Process-2')

# Start the processes
start = time.time()
process1.start()
process2.start()

# Wait for both processes to finish
process1.join()
process2.join()

end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")
