tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# 1. Print a list of uncompleted tasks
def uncompleted_tasks(list):
    uncompleted_tasks_list = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks_list.append(task["description"])
    return print(uncompleted_tasks_list)

uncompleted_tasks(tasks)

# 2. Print a list of completed tasks
def completed_tasks(list):
    completed_tasks_list = []
    for task in list:
        if task["completed"] == True:
            completed_tasks_list.append(task["description"])
    return print (completed_tasks_list)

completed_tasks(tasks)

# 3. Print a list of all task descriptions
def task_description(list):
    task_list = []
    for task in list:
        task_list.append(task["description"])
    return print(task_list)

task_description(tasks)

# 4. Print a list of tasks where time_taken is at least a given time
def timed_tasks(list, input_time):
    timed_list = []
    for time in list:
        if input_time <= time["time_taken"]:
            timed_list.append(time["description"])
    return print(timed_list)

timed_tasks(tasks, 15)

# 5. Print any task with a given description
def name_task(list, task_name):
    for name in list:
        if task_name == name["description"]:
            print(name)

name_task(tasks, "Feed Cat")