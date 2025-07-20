print("THIS IS YOUR TASK MANAGER!")
task_list = []

print("1. Add Task")
print("2. View Task")
print("3. Delete Task")
print("4. Exit")

ans = input("Enter your choice: ")



if ans == "1":
    for i in range(1, 101):
        task = input(f"Enter your task {i} (type '4' to stop): ")
        if task == "4":
            break
        task_list.append(task)

    # Check existing number of lines in file
    with open(r"C:\Users\Johnny Depp\OneDrive\Documents\python\task.txt", "r") as file_check:
         existing_lines = file_check.readlines()
         line_count = len(existing_lines)


    # Append new tasks with correct numbering
    with open(r"C:\Users\Johnny Depp\OneDrive\Documents\python\task.txt", "a") as file:
        for i, task in enumerate(task_list, start=line_count + 1):  ###  i is index and task is value
            file.write(f"{i}. {task}\n")

    print("These are your total tasks:")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task}")


elif(ans == "2"):
    print("this are your total task")    
    with open(r"C:\Users\Johnny Depp\OneDrive\Documents\python\task.txt","r") as file:
     stuff = file.read()
     print(stuff)
    

    
elif(ans=="3"):
    print("this are your total task")    
    with open(r"C:\Users\Johnny Depp\OneDrive\Documents\python\task.txt","r") as file2:
     stuff = file2.read()
     print(stuff)
    del_line = int(input("which task you want to delete?? "))
    with open(r"C:\Users\Johnny Depp\OneDrive\Documents\python\task.txt","r") as file:
        existing_lines = file.readlines()
        
        del existing_lines[del_line-1]
        with open(r"C:\Users\Johnny Depp\OneDrive\Documents\python\task.txt","w") as file_for_write:
            for i, task in enumerate(existing_lines, start=1):
                file_for_write.write(f"{i}.{task.split(".",1)[1]}")
    file.close()
    print("thi is your final result...")
    with open(r"C:\Users\Johnny Depp\OneDrive\Documents\python\task.txt","r") as file:
     stuff = file.read()
     print(stuff)