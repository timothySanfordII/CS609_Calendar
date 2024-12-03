from tkinter import Tk, Label, Button, Text, Frame, Entry, Listbox, Toplevel, END, SINGLE
from datetime import datetime
from database import setup_database, get_events_for_month
from navigation import prev_month, next_month, get_calendar
from events import add_event_logic, edit_event_logic, delete_event_logic
import holidays

# Function to display calendar
def show_calendar():
    global current_year, current_month
    cal = get_calendar(current_year, current_month)
    calendar_display.delete(1.0, "end")
    calendar_display.insert("end", cal)
    show_events()
    show_holidays()

# Function to navigate months
def prev_month_action():
    global current_year, current_month
    current_year, current_month = prev_month(current_year, current_month)
    show_calendar()

def next_month_action():
    global current_year, current_month
    current_year, current_month = next_month(current_year, current_month)
    show_calendar()

# Function to manually jump to a specific month and year
def go_to_month():
    global current_year, current_month
    try:
        entered_year = int(year_entry.get())
        entered_month = int(month_entry.get())
        if 1 <= entered_month <= 12:
            current_year = entered_year
            current_month = entered_month
            show_calendar()
        else:
            error_label.config(text="Invalid month! Enter a value between 1 and 12.")
    except ValueError:
        error_label.config(text="Invalid input! Please enter valid numbers.")

# Display events for the current month
def show_events():
    global current_year, current_month
    event_list.delete(0, END)
    month_events = get_events_for_month(current_year, current_month)
    for event in month_events:
        event_list.insert(END, f"{event[1]}: {event[2]}")

# Display holidays for the current month
def show_holidays():
    global current_year, current_month
    us_holidays = holidays.US(years=current_year)
    month_holidays = [holiday for holiday in us_holidays if holiday.year == current_year and holiday.month == current_month]
    holiday_list.delete(0, END)
    for holiday in month_holidays:
        holiday_date = holiday
        holiday_name = us_holidays.get(holiday)
        holiday_list.insert(END, f"{holiday_date.day:2d} - {holiday_name}")

# Add a new event
def add_event():
    def save_event():
        event_date = event_date_entry.get()
        event_description = event_description_entry.get()
        if add_event_logic(event_date, event_description, current_year, current_month):
            show_events()
            event_window.destroy()
        else:
            error_label.config(text="Date must be in the current month and year!")

    event_window = Toplevel(root)
    event_window.title("Add Event")
    event_window.geometry("300x200")

    Label(event_window, text="Event Date (YYYY-MM-DD):").pack(pady=5)
    event_date_entry = Entry(event_window, width=25)
    event_date_entry.pack(pady=5)

    Label(event_window, text="Event Description:").pack(pady=5)
    event_description_entry = Entry(event_window, width=25)
    event_description_entry.pack(pady=5)

    error_label = Label(event_window, text="", fg="red")
    error_label.pack(pady=5)

    save_button = Button(event_window, text="Save", command=save_event)
    save_button.pack(pady=10)

# Edit an existing event
def edit_event():
    selected_index = event_list.curselection()
    if not selected_index:
        return  # No item selected

    event_id, event_date, event_description = get_events_for_month(current_year, current_month)[selected_index[0]]

    def save_edited_event():
        new_date = event_date_entry.get()
        new_description = event_description_entry.get()
        try:
            edit_event_logic(event_id, new_date, new_description)
            show_events()
            edit_window.destroy()
        except ValueError:
            error_label.config(text="Invalid date format! Use YYYY-MM-DD.")

    edit_window = Toplevel(root)
    edit_window.title("Edit Event")
    edit_window.geometry("300x200")

    Label(edit_window, text="Edit Event Date (YYYY-MM-DD):").pack(pady=5)
    event_date_entry = Entry(edit_window, width=25)
    event_date_entry.insert(0, event_date)
    event_date_entry.pack(pady=5)

    Label(edit_window, text="Edit Event Description:").pack(pady=5)
    event_description_entry = Entry(edit_window, width=25)
    event_description_entry.insert(0, event_description)
    event_description_entry.pack(pady=5)

    error_label = Label(edit_window, text="", fg="red")
    error_label.pack(pady=5)

    save_button = Button(edit_window, text="Save", command=save_edited_event)
    save_button.pack(pady=10)

# Delete an event
def delete_event():
    selected_index = event_list.curselection()
    if not selected_index:
        return  # No item selected

    event_id = get_events_for_month(current_year, current_month)[selected_index[0]][0]
    delete_event_logic(event_id)
    show_events()

# Main Tkinter window
root = Tk()
root.title("Interactive Calendar with Events")
root.geometry("600x800")

# Navigation frame
nav_frame = Frame(root)
nav_frame.pack(pady=5)

prev_button = Button(nav_frame, text="⬅", command=prev_month_action, font=("Arial", 12))
prev_button.pack(side="left", padx=20)

next_button = Button(nav_frame, text="➡", command=next_month_action, font=("Arial", 12))
next_button.pack(side="right", padx=20)

# Manual month/year entry
entry_frame = Frame(root)
entry_frame.pack(pady=10)

Label(entry_frame, text="Month:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
month_entry = Entry(entry_frame, width=5, font=("Arial", 12))
month_entry.grid(row=0, column=1, padx=5)

Label(entry_frame, text="Year:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
year_entry = Entry(entry_frame, width=8, font=("Arial", 12))
year_entry.grid(row=0, column=3, padx=5)

go_button = Button(entry_frame, text="Go", command=go_to_month, font=("Arial", 12))
go_button.grid(row=0, column=4, padx=10)

error_label = Label(root, text="", fg="red", font=("Arial", 10))
error_label.pack(pady=5)

# Calendar Display
calendar_display = Text(root, width=40, height=10, font=("Courier", 12))
calendar_display.pack(pady=10)

# Events display
Label(root, text="Events for the Month", font=("Arial", 14)).pack(pady=5)

event_list = Listbox(root, width=50, height=5, font=("Courier", 10), selectmode=SINGLE)
event_list.pack(pady=5)

button_frame = Frame(root)
button_frame.pack(pady=5)

add_button = Button(button_frame, text="Add Event", command=add_event, font=("Arial", 12))
add_button.pack(side="left", padx=10)

edit_button = Button(button_frame, text="Edit Event", command=edit_event, font=("Arial", 12))
edit_button.pack(side="left", padx=10)

delete_button = Button(button_frame, text="Delete Event", command=delete_event, font=("Arial", 12))
delete_button.pack(side="left", padx=10)

# Holidays display
Label(root, text="Holidays for the Month", font=("Arial", 14)).pack(pady=5)

holiday_list = Listbox(root, width=50, height=5, font=("Courier", 10))
holiday_list.pack(pady=10)

# Initialize database and calendar
setup_database()
current_year = datetime.now().year
current_month = datetime.now().month
show_calendar()

root.mainloop()