import tkinter as tk
from tkinter import messagebox

# setup main window
root = tk.Tk()
root.title("Student Reminder App")
root.geometry("500x650")

# empty lists for storing information
reminders = []
study_plan = []

# Stores the reminder and study plan currently being edited
editing_reminder = -1
editing_study_plan = -1

# Home page functions
def open_notification():
    home_frame.pack_forget() # .pack_forget() hides the home page once the notification page is opened
    notification_frame.pack()

def open_study_planner():
    home_frame.pack_forget()
    study_frame.pack()

def back_home_notification():
    notification_frame.pack_forget()
    home_frame.pack()

def back_home_study():
    study_frame.pack_forget()
    home_frame.pack()

# Reminder functions
def show_reminders(): # this function refreshes the reminder list after adding, deleting or editing
    reminder_list.delete("1.0", tk.END) # removes everything currently in the text box
    for i in range(len(reminders)): # counts the reminders in the list
        reminder_list.insert(tk.END,str(i + 1) + ". " + reminders[i] + "\n\n") # adds each reminder to the text box

# gets the information entered by the user
def add_reminder():
    subject = subject_entry.get()
    equipment = equipment_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    # checks if the user has left any information empty
    if subject == '' or equipment == '' or date == '' or time == '':
        messagebox.showerror('Error!','Please fill in all the information!') # shows an error message if information is missing
    else:
        reminder = ('Subject: ' + subject +'\nEquipment: ' + equipment +'\nDate: ' + date +'\nTime: ' + time)
        reminders.append(reminder)
        show_reminders() # refreshes the reminder list

        # clears the Entry boxes after adding the reminder
        subject_entry.delete(0, tk.END)
        equipment_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

        messagebox.showinfo("Success","Reminder added successfully!")

def edit_reminder():
    global editing_reminder
    number = number_entry.get()
    if number == '':
        messagebox.showerror('Error!','Please enter a reminder number!')
    else:
        number = int(number) # changes the number from text into an integer
        if number < 1 or number > len(reminders): # check if the number is less than 1 or larger than the length of reminders
            messagebox.showerror('Error!','That reminder does not exist!')
        else:
            editing_reminder = number - 1 # stores which reminder the user wants to edit
            reminder = reminders[editing_reminder] # gets the selected reminder
            information = reminder.split('\n') # separates the reminder information

            # puts the old information back into the Entry boxes
            subject_entry.delete(0, tk.END)
            subject_entry.insert(0,information[0].replace('Subject: ', ''))

            equipment_entry.delete(0, tk.END)
            equipment_entry.insert(0,information[1].replace('Equipment: ', ''))

            date_entry.delete(0, tk.END)
            date_entry.insert(0,information[2].replace('Date: ', ''))

            time_entry.delete(0, tk.END)
            time_entry.insert(0,information[3].replace('Time: ', ''))

            messagebox.showinfo('Edit Reminder','Change the information and click Save Changes.')

def save_changes():
    global editing_reminder
    if editing_reminder == -1:
        messagebox.showerror('Error!','Please click Edit Reminder first!')
    else:
        # gets the new information from the Entry boxes
        subject = subject_entry.get()
        equipment = equipment_entry.get()
        date = date_entry.get()
        time = time_entry.get()

        if subject == '' or equipment == '' or date == '' or time == '':
            messagebox.showerror('Error!','Please fill in all the information!')
        else:
            reminder = ('Subject: ' + subject +'\nEquipment: ' + equipment +'\nDate: ' + date +'\nTime: ' + time)
            reminders[editing_reminder] = reminder # replaces the old reminder with the new one
            show_reminders()
            editing_reminder = -1 # shows that editing has finished

            # clears the Entry boxes
            subject_entry.delete(0, tk.END)
            equipment_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            time_entry.delete(0, tk.END)
            number_entry.delete(0, tk.END)

            messagebox.showinfo('Success','Reminder updated successfully!')

def delete_reminder():
    number = number_entry.get()
    if number == '':
        messagebox.showerror('Error!','Please enter a reminder number!')
    else:
        number = int(number)
        if number < 1 or number > len(reminders):
            messagebox.showerror('Error!','That reminder does not exist!')
        else:
            reminders.pop(number - 1) # removes the selected reminder
            show_reminders()
            number_entry.delete(0, tk.END) # clears the number Entry box
            messagebox.showinfo('Success','Reminder deleted successfully!')

# Study Period Planner functions
def show_study_plan():
    study_list.delete("1.0", tk.END)
    for i in range(len(study_plan)):
        study_list.insert(tk.END,str(i + 1) + ". " + study_plan[i] + "\n\n")

def add_study_plan():
    subject = study_subject_entry.get()
    task = study_task_entry.get()
    date = study_date_entry.get()
    time = study_time_entry.get()

    if subject == '' or task == '' or date == '' or time == '':
        messagebox.showerror('Error!','Please fill in all the information!')
    else:
        plan = ('Subject: ' + subject +'\nTask: ' + task + '\nDate: ' + date + '\nTime: ' + time)
        study_plan.append(plan) # adds the study plan into the list
        show_study_plan() # refreshes the study plan list

        # clears the Entry boxes after adding
        study_subject_entry.delete(0, tk.END)
        study_task_entry.delete(0, tk.END)
        study_date_entry.delete(0, tk.END)
        study_time_entry.delete(0, tk.END)

        messagebox.showinfo('Success','Study plan added successfully!')


def edit_study_plan():
    global editing_study_plan
    number = study_number_entry.get() # gets the study plan number entered by the user
    if number == '':
        messagebox.showerror('Error!','Please enter a study plan number!')
    else:
        number = int(number)
        if number < 1 or number > len(study_plan):
            messagebox.showerror('Error!','That study plan does not exist!')
        else:
            editing_study_plan = number - 1
            plan = study_plan[editing_study_plan]
            information = plan.split('\n')

            study_subject_entry.delete(0, tk.END)
            study_subject_entry.insert(0,information[0].replace('Subject: ', ''))

            study_task_entry.delete(0, tk.END)
            study_task_entry.insert(0,information[1].replace('Task: ', ''))

            study_date_entry.delete(0, tk.END)
            study_date_entry.insert(0,information[2].replace('Date: ', ''))

            study_time_entry.delete(0, tk.END)
            study_time_entry.insert(0,information[3].replace('Time: ', ''))

            messagebox.showinfo('Edit Study Plan','Change the information and click Save Changes.')

def save_study_plan_changes():
    global editing_study_plan
    if editing_study_plan == -1:
        messagebox.showerror('Error!','Please click Edit Study Plan first!')
    else:
        subject = study_subject_entry.get()
        task = study_task_entry.get()
        date = study_date_entry.get()
        time = study_time_entry.get()

        if subject == '' or task == '' or date == '' or time == '':
            messagebox.showerror('Error!','Please fill in all the information!')
        else:
            plan = ('Subject: ' + subject +'\nTask: ' + task +'\nDate: ' + date +'\nTime: ' + time)
            study_plan[editing_study_plan] = plan
            show_study_plan()
            editing_study_plan = -1

            # clears the Entry boxes
            study_subject_entry.delete(0, tk.END)
            study_task_entry.delete(0, tk.END)
            study_date_entry.delete(0, tk.END)
            study_time_entry.delete(0, tk.END)
            study_number_entry.delete(0, tk.END)

            messagebox.showinfo('Success','Study plan updated successfully!')

def delete_study_plan():
    number = study_number_entry.get() # gets the study plan number
    if number == '':
        messagebox.showerror('Error!','Please enter a study plan number!')
    else:
        number = int(number)
        if number < 1 or number > len(study_plan):
            messagebox.showerror('Error!','That study plan does not exist!')
        else:
            study_plan.pop(number - 1)
            show_study_plan()
            study_number_entry.delete(0, tk.END)
            messagebox.showinfo('Success','Study plan deleted successfully!')

# Study Period Planner page
study_frame = tk.Frame(root)
study_title = tk.Label(study_frame,text='Study Period Planner',font=('Arial', 18))
study_title.pack(pady=15)

tk.Label(study_frame,text='Subject').pack()
study_subject_entry = tk.Entry(study_frame)
study_subject_entry.pack()

tk.Label(study_frame,text='Task').pack()
study_task_entry = tk.Entry(study_frame)
study_task_entry.pack()

tk.Label(study_frame,text='Date').pack()
study_date_entry = tk.Entry(study_frame)
study_date_entry.pack()

tk.Label(study_frame,text='Time').pack()
study_time_entry = tk.Entry(study_frame)
study_time_entry.pack()

study_add_button = tk.Button(
    study_frame,
    text='Add Study Plan',
    command=add_study_plan
)
study_add_button.pack(pady=5)

# Study plan list
study_label = tk.Label(study_frame,text='Study Plan List')
study_label.pack()
study_list = tk.Text(study_frame,height=8,width=60)
study_list.pack()

# Edit and delete study plan
tk.Label(study_frame,text='Enter study plan number:').pack()
study_number_entry = tk.Entry(study_frame)
study_number_entry.pack()

study_edit_button = tk.Button(study_frame,text='Edit Study Plan',command=edit_study_plan)
study_edit_button.pack(pady=2)

study_save_button = tk.Button(study_frame,text='Save Changes',command=save_study_plan_changes)
study_save_button.pack(pady=2)

study_delete_button = tk.Button(study_frame,text='Delete Study Plan',command=delete_study_plan)
study_delete_button.pack(pady=2)

# Back to home button
study_home_button = tk.Button(study_frame,text='Back to Home',command=back_home_study)
study_home_button.pack(pady=5)

# Home page
home_frame = tk.Frame(root)
title = tk.Label(home_frame,text='Student Reminder App',font=('Arial', 20))
title.pack(pady=30)

open_button = tk.Button(home_frame,text='Daily Notification',command=open_notification)
open_button.pack(pady=5)

study_button = tk.Button(home_frame,text='Study Period Planner',command=open_study_planner)
study_button.pack(pady=5)

home_frame.pack()

# Daily Notification page
notification_frame = tk.Frame(root)

title2 = tk.Label(notification_frame,text='Daily Notification',font=('Arial', 18))
title2.pack(pady=15)

tk.Label(notification_frame,text='Subject').pack()
subject_entry = tk.Entry(notification_frame)
subject_entry.pack()

tk.Label(notification_frame,text='Equipment').pack()
equipment_entry = tk.Entry(notification_frame)
equipment_entry.pack()

tk.Label(notification_frame,text='Date').pack()
date_entry = tk.Entry(notification_frame)
date_entry.pack()

tk.Label(notification_frame,text='Time').pack()
time_entry = tk.Entry(notification_frame)
time_entry.pack()

add_button = tk.Button(notification_frame,text='Add Reminder',command=add_reminder)
add_button.pack(pady=5)


# Reminder list
reminder_label = tk.Label(notification_frame,text='Reminder List')
reminder_label.pack()
reminder_list = tk.Text(notification_frame,height=8,width=60)
reminder_list.pack()

# Edit and delete reminder
tk.Label(notification_frame,text='Enter reminder number:').pack()

number_entry = tk.Entry(notification_frame)
number_entry.pack()

edit_button = tk.Button(notification_frame,text='Edit Reminder',command=edit_reminder)
edit_button.pack(pady=2)

save_button = tk.Button(notification_frame,text='Save Changes',command=save_changes)
save_button.pack(pady=2)

delete_button = tk.Button(notification_frame,text='Delete Reminder',command=delete_reminder)
delete_button.pack(pady=2)

# Back to home button
home_notification_button = tk.Button(notification_frame,text='Back to Home',command=back_home_notification)
home_notification_button.pack(pady=5)


# Study Period Planner page
study_frame = tk.Frame(root)
study_title = tk.Label(study_frame,text='Study Period Planner',font=('Arial', 18))
study_title.pack(pady=15)

tk.Label(study_frame,text='Subject').pack()
study_subject_entry = tk.Entry(study_frame)
study_subject_entry.pack()

tk.Label(study_frame,text='Task').pack()
study_task_entry = tk.Entry(study_frame)
study_task_entry.pack()

tk.Label(study_frame,text='Date').pack()
study_date_entry = tk.Entry(study_frame)
study_date_entry.pack()

tk.Label(study_frame, text='Time').pack()
study_time_entry = tk.Entry(study_frame)
study_time_entry.pack()

study_add_button = tk.Button(study_frame,text='Add Study Plan',command=add_study_plan)
study_add_button.pack(pady=5)

# Study plan list
study_label = tk.Label(study_frame,text='Study Plan List')
study_label.pack()
study_list = tk.Text(study_frame,height=8,width=60)
study_list.pack()

# Back to home button
home_study_button = tk.Button(study_frame,text='Back to Home',command=back_home_study)
home_study_button.pack(pady=5)

# Function that closes the program
def finish():
    root.destroy()

# Finish button
finish_button = tk.Button(notification_frame,text='Finish',command=finish)
finish_button.pack()

root.mainloop()
