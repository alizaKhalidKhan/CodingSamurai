#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Internship @Coding Samurai - Task (1)
"""Project Title: To-Do List Application

Project Description: Create a simple command-line to-do list application in Python that
allows users to manage their tasks. This project will help you practice working with data
structures, user input, and basic file handling.

Key Features you can include:

>> Add tasks: Users should be able to add tasks to their to-do list with a title and a
description.
>> List tasks: Users can view their existing tasks with details like title, description, and a
unique task ID.
>> Mark tasks as complete: Users can mark tasks as complete or uncompleted.
>> Delete tasks: Users can remove tasks from their to-do list.
>> Save tasks: Implement file handling to save tasks to a text file, so users can retrieve them
even after closing the program.
>> Load tasks: Allow users to load their saved tasks from the text file when they start the
program.
>> User-friendly interface: Create a simple and intuitive command-line interface that
guides users through the available actions."""

#Menu-driven Program
#Datastructure : LinkedList 

import os

class TodoTask:
    
    def __init__(self, name, description):
        
        
        """
        Represents a task with its name and description.

        Args:
            name (str): The name of the task.
            description(str) : The description of the task.
        """
        
        self.name = name
        self.description = description
        self.completed = False
        self.next = None

class ToDoList:
        
    """
    
    To do list class handles the addition, displaying, searching, updation and deletion (CRUD) operations of the tasks.
    Along with saving and loading task data from the file
    
    """
    
    def __init__(self):
        
        self.head = None
        self.task_id_counter = 1              # Assign each task with a unique ID

    def addTask(self, task_name, task_description):
        
        """
        Adds a task to the to-do list.
        
        Args:
            task_name (str): The name of the task to be added.
            task_description (str) : The description of the task to be added.
        """
            
        new_task = TodoTask(task_name, task_description)
        new_task.id = self.task_id_counter
        self.task_id_counter += 1         #Increment Counter

        if self.head is None:
            self.head = new_task
        else:
            curNode = self.head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = new_task
        print("Task added successfully to the to-do list!")

    def deleteTask(self, task_id):
        
        """
        Deletes a task from the to-do-list using Task id.
        
        Args:
            task_id (int): The unique id of the task to be deleted.
        """
        
        if self.head is None:
            print("No tasks to delete!")
            return

        if self.head.id == task_id:
            self.head = self.head.next
            print("Task deleted successfully!")
            return

        curNode = self.head
        prev = None
        while curNode:
            if curNode.id == task_id:
                prev.next = curNode.next
                print("Task deleted successfully!")
                return
            prev = curNode
            curNode = curNode.next
        print("Task not found!")

    def searchTask(self, task_id):
        
        """
        Searches for a task in the to-do-list using task id.

        Args:
            task_id (int): The unique task id.
        """
        
        curNode = self.head
        while curNode:
            if curNode.id == task_id:
                return curNode
            curNode = curNode.next
        return None

    def displayTasks(self, show_completed=False):
        
                        
        """
        
        Displays all the tasks in the in the to-do-list.
        
        """
        
        if self.head is None:
            print("No tasks to display")
            return

        curNode = self.head
        while curNode:
            if show_completed or not curNode.completed:
                status = "Completed" if curNode.completed else "Not Completed"
                print(f"Task ID: {curNode.id} - Task: {curNode.name} - Status: {status}")
            curNode = curNode.next

    def markCompleted(self, task_id):
        
        
        """
        Marks a task complete in the to-do-list.

        Args:
            task_id (int): The id of the task.
        """
        
        task = self.searchTask(task_id)
        if task:
            task.completed = True
            print("Task marked as completed!")
        else:
            print("Task not found!")


    def saveTasks(self, filename="tasks.txt"):
        
        """ 
        Saves Tasks in the file
        
        """
        try:
            with open(filename, "w") as file:
                curNode = self.head
                while curNode is not None:
                    file.write(f"{curNode.name},{curNode.description},{curNode.completed},{curNode.id}\n")
                    curNode = curNode.next
            print("Tasks saved to file.")
        except Exception as e:
            print(f"Error while saving tasks: {e}")

    def loadTasks(self, filename="tasks.txt"):
        
        """
        
        Loads The tasks from the file
        
        """
        
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        task_data = line.strip().split(',')
                        if len(task_data) == 4:
                            task_name, task_description, task_completed, task_id = task_data
                            try:
                                new_task = TodoTask(task_name, task_description)
                                new_task.completed = bool(int(task_completed))
                                new_task.id = int(task_id)
                                if self.head is None:
                                    self.head = new_task
                                else:
                                    curNode = self.head
                                    while curNode.next is not None:
                                        curNode = curNode.next
                                    curNode.next = new_task
                            except ValueError:
                                print(f"Skipping invalid task data: {line}")
                print("Tasks loaded from file.")
            else:
                print("No saved tasks found in the file.")
        except Exception as e:
            print(f"Error while loading tasks: {e}")
            
            
def print_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Search Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Save Tasks to File")
    print("7. Load Tasks from File")
    print("8. Quit")
    print()

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            task_description = input("Enter the task description: ")
            todo_list.addTask(task_name, task_description)

        elif choice == "2":
            todo_list.displayTasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter the task ID to search: "))
                task = todo_list.searchTask(task_id)
                if task:
                    status = "Completed" if task.completed else "Not Completed"
                    print(f"Task found: Task ID: {task.id} - Task: {task.name} - Status: {status}")
                else:
                    print("Task not found!")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter the task ID to delete: "))
                todo_list.deleteTask(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "5":
            try:
                task_id = int(input("Enter the task ID to mark as completed: "))
                todo_list.markCompleted(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "6":
            todo_list.saveTasks()

        elif choice == "7":
            todo_list.loadTasks()

        elif choice == "8":
            print("Quitting the program...")
            break

        else:
            print("Invalid Input! Please try again.")


# In[ ]:





# In[ ]:




