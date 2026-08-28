import tkinter as tk
from tkinter import messagebox
import json

# setup main window
root = tk.Tk()
root.title("Student Reminder App")
root.geometry("550x680")

# empty lists for storing information
reminders = []
study_plan = []

# Saves reminders and study plans to a JSON file
def save_data():
    data = {"reminders": reminders,"study_plan": study_plan}
    with open("student_data.json", "w") as file:
        json.dump(data, file, indent=4)

# Loads reminders and study plans from the JSON file
def load_data():
    global reminders, study_plan
    try:
        with open("student_data.json", "r") as file:
            data = json.load(file)
        reminders = data.get("reminders", [])
        study_plan = data.get("study_plan", [])
    except FileNotFoundError:
        reminders = []
        study_plan = []

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

# Function that closes the program
def finish():
    root.destroy()

# Home page
home_frame = tk.Frame(root)
title = tk.Label(home_frame,text='Student Reminder App',font=('Arial', 20))
title.pack(pady=30)

open_button = tk.Button(home_frame,text='Daily Notification',command=open_notification,width=20,height=2)
open_button.pack(pady=5)

study_button = tk.Button(home_frame,text='Study Period Planner',command=open_study_planner,width=20,height=2)
study_button.pack(pady=5)

exit_button = tk.Button(home_frame,text='Exit',command=finish,width=20,height=2)
exit_button.pack(pady=5)

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
        save_data()
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
        try:
            number = int(number) # changes the number from text into an integer
        except ValueError:
            messagebox.showerror('Error!','Please enter a number') # tell theuser this input can only be an integer
            return
        if number < 1 or number > len(reminders): # check if the number is less than 1 or larger than the length of reminders
            messagebox.showerror('Error!','That reminder does not exist!')
        else:
            editing_reminder = number - 1
            reminder = reminders[editing_reminder]
            information = reminder.split('\n')

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
    global editing_reminder # global allows the function to change the variable(editing_reminder) that is outside this function
    if editing_reminder == -1:
        messagebox.showerror('Error!','Please click Edit Reminder first!')
    else:
        subject = subject_entry.get()
        equipment = equipment_entry.get()
        date = date_entry.get()
        time = time_entry.get()

        if subject == '' or equipment == '' or date == '' or time == '':
            messagebox.showerror('Error!','Please fill in all the information!')
        else:
            reminder = ('Subject: ' + subject +'\nEquipment: ' + equipment +'\nDate: ' + date +'\nTime: ' + time)
            reminders[editing_reminder] = reminder
            save_data()
            show_reminders()
            editing_reminder = -1

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
        try:
            number = int(number)
        except ValueError:
            messagebox.showerror('Error!','Please enter a number')
            return
        if number < 1 or number > len(reminders):
            messagebox.showerror('Error!','That reminder does not exist!')
        else:
            answer = messagebox.askyesno('Confirm Delete','Are you sure you want to delete this reminder?') # ask the user to confirm before deleting
            if answer:
                reminders.pop(number - 1) # removes the selected reminder
                save_data()
                show_reminders()
                number_entry.delete(0, tk.END)
                messagebox.showinfo('Success','Reminder deleted successfully!')

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

edit_button = tk.Button(notification_frame,text='Edit Reminder',command=edit_reminder,width=20,height=2)
edit_button.pack(pady=2)

save_button = tk.Button(notification_frame,text='Save Changes',command=save_changes,width=20,height=2)
save_button.pack(pady=2)

delete_button = tk.Button(notification_frame,text='Delete Reminder',command=delete_reminder,width=20,height=2)
delete_button.pack(pady=2)

# Back to home button
home_notification_button = tk.Button(notification_frame,text='Back to Home',command=back_home_notification,width=20,height=2)
home_notification_button.pack(pady=5)

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
        study_plan.append(plan)
        save_data()
        show_study_plan()

        study_subject_entry.delete(0, tk.END)
        study_task_entry.delete(0, tk.END)
        study_date_entry.delete(0, tk.END)
        study_time_entry.delete(0, tk.END)

        messagebox.showinfo('Success','Study plan added successfully!')

def edit_study_plan():
    global editing_study_plan
    number = study_number_entry.get()
    if number == '':
        messagebox.showerror('Error!','Please enter a study plan number!')
    else:
        try:
            number = int(number)
        except ValueError:
            messagebox.showerror('Error!','Please enter a number')
            return
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
            save_data()
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
    number = study_number_entry.get()
    if number == '':
        messagebox.showerror('Error!','Please enter a study plan number!')
    else:
        try:
            number = int(number)
        except ValueError:
            messagebox.showerror('Error!','Please enter a number')
            return
        if number < 1 or number > len(study_plan):
            messagebox.showerror('Error!','That study plan does not exist!')
        else:
            answer = messagebox.askyesno('Confirm Delete','Are you sure you want to delete this study plan?')
            if answer:
                study_plan.pop(number - 1)
                save_data()
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

study_add_button = tk.Button(study_frame,text='Add Study Plan',command=add_study_plan)
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

study_edit_button = tk.Button(study_frame,text='Edit Study Plan',command=edit_study_plan,width=20,height=2)
study_edit_button.pack(pady=2)

study_save_button = tk.Button(study_frame,text='Save Changes',command=save_study_plan_changes,width=20,height=2)
study_save_button.pack(pady=2)

study_delete_button = tk.Button(study_frame,text='Delete Study Plan',command=delete_study_plan,width=20,height=2)
study_delete_button.pack(pady=2)

# Back to home button
study_home_button = tk.Button(study_frame,text='Back to Home',command=back_home_study,width=20,height=2)
study_home_button.pack(pady=5)

# Load saved information when the program starts
load_data()
show_reminders()
show_study_plan()

root.mainloop()
