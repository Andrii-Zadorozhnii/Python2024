"""
Task 6 Final Exersice: Time Tracker for Tasks

Objective

You work for a project management company, and they want to offer a simple time tracker for their clients. The tool will let users log the cumber of hours spent on different tasks and then provide a summary at the end.

Introductions

1. Create a list called tasks and populate it with initial tasks: "Planning","Design","Codding","Testing".
2.  Create another list called time_spent to shore the time spent on each task. Initialize it with zeros.
3. Create a function called log_time that takes a task name and an amount of time. It will find the task in the tasks list and update the corresponding in time_spent.
4.  Use while loop to repeatedly ask the user for a task and time spent on that task until they choose to exit.
5.  Use for loop to go through the task and time_spent lists, printing out a summary of time spent on each task.

"""

tasks = ["planning", "design", "codding", "testing"]
time_spent = [0, 0, 0, 0]

def log_time(tasks,time):
    for i in tasks(len(tasks)):
        if tasks[i] == tasks:
            time_spent[i] += time

while True:
    print(f'Tasks {tasks}')
    task = input('Enter a task to log time for it / or enter enter for exit')

    if task == "exit":
        break
    else:
        if task in tasks:
            time = float(input("How many hours did you spend on this tak? \n"))
            log_time(task, time)
        else:
            print("We coudn't find this task")

for i in range(len(tasks)):
    print(f'Task: {task[i]}, hours spent: time_spent[i')