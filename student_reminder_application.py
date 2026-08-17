import tkinter as tk
from tkinter import messagebox

# setup main window
root = tk.Tk()
root.title("Student Reminder App")
root.geometry("500x500")

# stores all reminders
reminders = []

def open_notification():
    home_frame.pack_forget() # this code hides the home page once notification page is opened
    notification_frame.pack()

# ask user to enter their reminder information
def add_reminder():
    subject = subject_entry.get()
    equipment = equipment_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    if subject == '' or equipment == '' or date == '' or tiem == '': # use if statement to check if the user has leave the input empty
        messagebox.showerror('Error!', 'Please fill in all the information!') # shows error message if the user entered nothing

    else:
        reminder = 'Subject: ' + subject + '\n' + 'Equipment: ' + equipment + '\n' + 'Date: ' + date + '\n' + 'Time: ' + time

        reminders.append(reminder) # add the reminder into the remidners list

        reminder_list.insert(tk.END,reminder + '\n\n')
        messagebox.showinfo('Success','Reminder added successfully!')

# Home page
home_frame = tk.Frame(root)

title = tk.Label(home_frame,text='Student Reminder App',font=('Arial',20))
title.pack(pady=30)

open_button = tk.Button(home_frame,text='Daily Notification',command=open_notification)
open_button.pack()

home_frame.pack()

# Daily Notification page
notification_frame = tk.Frame(root)

title2 = tk.Label(notification_frame,text='Daily Notification',font=('Arial',18))
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
add_button.pack()

# Reminder list
reminder_label = tk.Label(notification_frame,text='Reminder list')
reminder_label.pack()

reminder_list = tk.Text(notification_frame,height=8,width=60)
reminder_list.pack()

# function that closes the program
def finish():
    root.destroy()

# Finish button
finish_button = tk.Button(notification_frame,text='Finish',command=finish)
finish_button.pack()

root.mainloop()                
