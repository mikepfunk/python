'''
Create a Python program to remind me of my tasks, when I enter them, this
program will remind me.  I think it will do it after my day has ended, and
on the day it is due.  Maybe I will have it create a file, and add them to
and excel, csv file.  Then try to integrate it with my calendars.
'''
tasks = ''

while tasks != 'q':
    tasks = input("Enter your tasks or 'q' to quit: ")
    if tasks == 'q':
        break
    elif tasks != 'q':
        
        print(f"Your tasks are: {tasks}")
        with open('tasks.txt', 'a') as file:
            file.write(tasks + '\n')
        print("Your tasks have been saved.")
        print(tasks)