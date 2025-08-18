The Global Interpreter Lock (GIL) in Python is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes simultaneously in the same process. This means that even in a multi-threaded Python program, only one thread can execute Python code at a time. 

Here's a simple example to illustrate how the GIL affects multi-threading in Python:

### Example Without GIL Impact
This example shows a simple CPU-bound task performed in a multi-threaded environment.

```python
import threading
import time

def cpu_bound_task():
    start = time.time()
    for _ in range(10000000):
        pass  # some CPU-bound operation
    end = time.time()
    print(f"Thread {threading.current_thread().name} finished in {end - start:.2f} seconds")

# Create two threads
thread1 = threading.Thread(target=cpu_bound_task, name='Thread-1')
thread2 = threading.Thread(target=cpu_bound_task, name='Thread-2')

# Start the threads
start = time.time()
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")
```

### Example With GIL Impact
In this example, we show how the GIL can limit the performance of a multi-threaded program with CPU-bound tasks.

```python
import threading
import time

def cpu_bound_task():
    start = time.time()
    for _ in range(100000000):
        pass  # some CPU-bound operation
    end = time.time()
    print(f"Thread {threading.current_thread().name} finished in {end - start:.2f} seconds")

# Create two threads
thread1 = threading.Thread(target=cpu_bound_task, name='Thread-1')
thread2 = threading.Thread(target=cpu_bound_task, name='Thread-2')

# Start the threads
start = time.time()
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")
```

### Explanation
- **CPU-Bound Task**: The function `cpu_bound_task` performs a simple loop that simulates a CPU-bound operation.
- **Multi-Threading**: We create two threads, `thread1` and `thread2`, to run the `cpu_bound_task` function concurrently.
- **Time Measurement**: We measure the time taken by each thread to complete the task and the total time taken by the entire program.

Due to the GIL, even though we have two threads running in parallel, only one thread can execute Python bytecode at a time. As a result, the time taken by the multi-threaded version may not be significantly better (and could be worse) than running the tasks sequentially.

### Key Points
- **GIL and CPU-Bound Tasks**: For CPU-bound tasks, the GIL can be a bottleneck, as it limits the execution of bytecode to one thread at a time.
- **I/O-Bound Tasks**: For I/O-bound tasks (e.g., reading/writing to a file, network operations), multi-threading can still be beneficial, as the GIL is released during I/O operations.
- **Multiprocessing**: To bypass the GIL for CPU-bound tasks, you can use the `multiprocessing` module, which creates separate processes with their own memory space and separate GILs.

Here's an example of using the `multiprocessing` module to parallelize a CPU-bound task:

```python
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
```

In this example, the tasks are executed in parallel without being affected by the GIL.