# import threading
# import time

# def cpu_bound_task():
#     start = time.time()
#     for _ in range(10000000):
#         pass  # some CPU-bound operation
#     end = time.time()
#     print(f"Thread {threading.current_thread().name} finished in {end - start:.2f} seconds")

# # Create two threads
# thread1 = threading.Thread(target=cpu_bound_task, name='Thread-1')
# thread2 = threading.Thread(target=cpu_bound_task, name='Thread-2')

# # Start the threads
# start = time.time()
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

# end = time.time()
# print(f"Total time taken: {end - start:.2f} seconds")


# import threading
# import time

# def cpu_bound_task():
#     start = time.time()
#     for _ in range(100000000):
#         pass  # some CPU-bound operation
#     end = time.time()
#     print(f"Thread {threading.current_thread().name} finished in {end - start:.2f} seconds")

# # Create two threads
# thread1 = threading.Thread(target=cpu_bound_task, name='Thread-1')
# thread2 = threading.Thread(target=cpu_bound_task, name='Thread-2')

# # Start the threads
# start = time.time()
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

# end = time.time()
# print(f"Total time taken: {end - start:.2f} seconds")




import multiprocessing
import time

def cpu_bound_task():
    start = time.time()
    for _ in range(100000000):
        pass  # some CPU-bound operation
    end = time.time()
    print(f"Process {multiprocessing.current_process().name} finished in {end - start:.2f} seconds")

if __name__ == '__main__':
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
