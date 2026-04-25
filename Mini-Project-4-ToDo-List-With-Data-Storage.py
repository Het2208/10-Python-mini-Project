# def addTask(task,task_List):
#     task_List.append(task)
#     print(f"{task} has been added to the To-Do list.")
#
# def viewTask(task_List):
#     print("-" * 45)
#     for task in task_List:
#         print(task)
#
# def doneTask(donetask,task_List):
#     task_List.remove(donetask)
#     print(f"{donetask} Completed")
#     with open("Tasks.txt", "a") as file:
#         file.write(f"{donetask}\n")
#
# def deleteTask(deletetask , task_List):
#     task_List.remove(deletetask)
#     print(f"{deletetask} has been removed from the To-Do list.")
#
# def updateTask(changeTask , UpdatedTask , task_List):
#     task_List.update(changeTask , UpdatedTask)
#     print(f"{updateTask} has been updated to the To-Do list.")
#
# def viewCompletedTask():
#     print("#"*35)
#     with open("Tasks.txt", "r") as file:
#         lines = file.readlines()
#         for line in lines:
#             print(line)
#
#
# def main():
#     print("*" * 40)
#     print("Welcome to To-Do list!")
#     print("*" * 40)
#
#     is_running = True
#     task_List = []
#     while is_running:
#         print("-" * 45)
#         print("What would you like to do?")
#         print("1. Add Task \n2. View Tasks \n3. Mark Task as Done \n4. Delete Task \n5. Update task \n6. View Completed Task\n7. Exit")
#         print("-" * 45)
#         try:
#              ch = int(input("Enter a choice: "))
#         except ValueError:
#             print("Please enter a number.")
#
#
#         match(ch):
#             case 1:
#                 task = input("Enter Task Name: ")
#                 addTask(task , task_List)
#             case 2:
#                 viewTask(task_List)
#             case 3:
#                 tDone = input("Enter a task name that is done")
#                 if tDone in task_List:
#                     doneTask(tDone, task_List)
#                 else:
#                     print("Task not found!")
#             case 4:
#                 dTask = input("Enter a task name that you want to delete")
#                 if dTask in task_List:
#                     deleteTask(dTask, task_List)
#                 else:
#                     print("Task not found!")
#             case 5:
#                 changeTask = input("Enter a task name that you want to update")
#                 if changeTask in task_List:
#                     uTask = input("Enter a updated task name")
#                     updateTask(changeTask,uTask,task_List)
#                 else:
#                     print("Task not found!")
#             case 6:
#                 viewCompletedTask()
#             case 7:
#                 is_running = False
#             case _:
#                 print("That is not a valid choice.")
#
# main()

def addTask(task, task_List):
    task_List.append(task)
    saveTasks(task_List)
    print(f"{task} has been added to the To-Do list.")


def viewTask(task_List):
    print("-" * 45)
    if not task_List:
        print("No tasks available.")
    else:
        for i, task in enumerate(task_List, start=1):
            print(f"{i}. {task}")


def doneTask(donetask, task_List):
    task_List.remove(donetask)
    saveTasks(task_List)
    print(f"{donetask} completed!")

    with open("CompletedTasks.txt", "a") as file:
        file.write(donetask + "\n")


def deleteTask(deletetask, task_List):
    task_List.remove(deletetask)
    saveTasks(task_List)
    print(f"{deletetask} has been removed.")


def updateTask(oldTask, newTask, task_List):
    index = task_List.index(oldTask)
    task_List[index] = newTask
    saveTasks(task_List)
    print(f"{oldTask} updated to {newTask}.")


def viewCompletedTask():
    print("#" * 35)
    try:
        with open("CompletedTasks.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No completed tasks found.")


def saveTasks(task_List):
    with open("Tasks.txt", "w") as file:
        for task in task_List:
            file.write(task + "\n")


def loadTasks():
    tasks = []
    try:
        with open("Tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks


def main():
    print("*" * 40)
    print("Welcome to To-Do list!")
    print("*" * 40)

    is_running = True
    task_List = loadTasks()

    while is_running:
        print("-" * 45)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. View Completed Task")
        print("7. Exit")
        print("-" * 45)

        try:
            ch = int(input("Enter a choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        match ch:
            case 1:
                task = input("Enter Task Name: ")
                addTask(task, task_List)

            case 2:
                viewTask(task_List)

            case 3:
                tDone = input("Enter completed task name: ")
                if tDone in task_List:
                    doneTask(tDone, task_List)
                else:
                    print("Task not found!")

            case 4:
                dTask = input("Enter task name to delete: ")
                if dTask in task_List:
                    deleteTask(dTask, task_List)
                else:
                    print("Task not found!")

            case 5:
                changeTask = input("Enter task name to update: ")
                if changeTask in task_List:
                    uTask = input("Enter updated task name: ")
                    updateTask(changeTask, uTask, task_List)
                else:
                    print("Task not found!")

            case 6:
                viewCompletedTask()

            case 7:
                print("Exiting...")
                is_running = False

            case _:
                print("Invalid choice!")


main()
