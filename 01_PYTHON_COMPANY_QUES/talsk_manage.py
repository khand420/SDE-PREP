import heapq

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"Task(description={self.description}, priority={self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        heapq.heappush(self.tasks, task)
        print(f"Added: {task}")

    def get_task(self):
        if self.tasks:
            task = heapq.heappop(self.tasks)
            print(f"Retrieved: {task}")
            return task
        else:
            print("No tasks available.")
            return None

    def view_tasks(self):
        if self.tasks:
            print("Tasks in the queue:")
            for task in self.tasks:
                print(task)
        else:
            print("No tasks in the queue.")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Write documentation", 2)
    manager.add_task("Fix bugs", 1)
    manager.add_task("Implement new feature", 3)
    
    manager.view_tasks()
    
    manager.get_task()
    manager.view_tasks()
    
    manager.get_task()
    manager.view_tasks()
    
    manager.get_task()
    manager.view_tasks()
