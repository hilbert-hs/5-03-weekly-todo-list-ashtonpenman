# 5.03 Weekly ToDo List

todos = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
    }

def add(day, task, todos):
    if day in todos:
        todos[day].append(task)
        print(f"You have added {task} to {day}")
    else:
        print("what?")

def get(day, todos):
    if day in todos:
        print(f"You have to {todos[day]} on {day}.")

while True:
    descision = input("What would you like to do? (add/get/quit) ")
    day = input("What day would you like to update/get? ")
    if descision == "add":
        task = input("What task would you like to add? ")
        add(day, task, todos)
    elif descision == "get":
        get(day, todos)
    elif descision == "quit":
        pass