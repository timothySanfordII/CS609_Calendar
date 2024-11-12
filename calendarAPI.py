import calendar
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import requests

API_KEY = 'N8UYALLyNbsAFVw6BuV67HrogloGQrzs'
LOCATION = 'US'  # Use country code for holidays (e.g., 'US' for United States)

# Dictionary to store events, keys are "YYYY-MM-DD" strings, values are lists of events
events = {}
holiday_data = {}

def get_holidays_for_month(year, month):
    """Fetch holidays data for the specified year and month."""
    global holiday_data

    # Format month and year to fetch the holidays
    month_str = f"{month:02d}"
    year_str = str(year)

    # Check if holidays data for this month is already fetched
    if f"{year_str}-{month_str}" in events:
        return events[f"{year_str}-{month_str}"]

    try:
        # Request holiday data from the API
        url = f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country={LOCATION}&year={year}&month={month}"
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request failed

        # Parse JSON response
        holidays = response.json().get('response', {}).get('holidays', [])

        # Print the response to debug
        print(f"Fetched Holidays for {month}/{year}: {holidays}")
        
        # Store holidays data in dictionary by year-month key
        holidays_list = [holiday['name'] for holiday in holidays]
        events[f"{year_str}-{month_str}"] = holidays_list

        # Add holidays to the global events dictionary to display them on the calendar
        for holiday in holidays_list:
            event_date = f"{year_str}-{month_str}"
            events.setdefault(event_date, []).append(holiday)

        return holidays_list
    except requests.RequestException as e:
        print(f"Error fetching holidays: {e}")
        return []

def show_calendar(year, month):
    # Clear any previous calendar display
    for widget in calendar_frame.winfo_children():
        widget.destroy()
    
    # Add weekday headers
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days_of_week):
        lbl = tk.Label(calendar_frame, text=day, font=("Arial", 10, "bold"), borderwidth=1, relief="solid")
        lbl.grid(row=0, column=i, sticky="nsew")
    
    # Get calendar month data and display it with events
    month_days = calendar.monthcalendar(year, month)
    holidays = get_holidays_for_month(year, month)  # Get holidays for the month
    for week_num, week in enumerate(month_days):
        for day_num, day in enumerate(week):
            if day == 0:
                day_text = ""
                event_text = ""
            else:
                day_text = str(day)
                event_date = f"{year}-{month:02}-{day:02}"
                # Combine user events and holidays
                event_text = "\n".join(events.get(event_date, []))  # Join all events for the day
            
            # Label for each day, showing the day and any events
            lbl = tk.Label(calendar_frame, text=f"{day_text}\n{event_text}", font=("Arial", 10), 
                           borderwidth=1, relief="solid", justify="left")
            lbl.grid(row=week_num + 1, column=day_num, sticky="nsew")
            # Bind left-click to add events
            lbl.bind("<Button-1>", lambda e, d=day: add_event(year, month, d) if d != 0 else None)
    
    # Configure rows and columns to expand with window resizing
    for i in range(len(month_days) + 1):
        calendar_frame.rowconfigure(i, weight=1)
    for i in range(7):  # 7 columns for the days of the week
        calendar_frame.columnconfigure(i, weight=1)

def update_calendar():
    year = int(year_combobox.get())
    month = month_names.index(month_combobox.get()) + 1
    show_calendar(year, month)

def on_month_change(event):
    update_calendar()

def on_year_change(event):
    update_calendar()

def previous_month():
    month_index = month_names.index(month_combobox.get())
    if month_index == 0:  # Move to December of the previous year
        month_combobox.set(month_names[11])
        year_combobox.set(int(year_combobox.get()) - 1)
    else:
        month_combobox.set(month_names[month_index - 1])
    update_calendar()

def next_month():
    month_index = month_names.index(month_combobox.get())
    if month_index == 11:  # Move to January of the next year
        month_combobox.set(month_names[0])
        year_combobox.set(int(year_combobox.get()) + 1)
    else:
        month_combobox.set(month_names[month_index + 1])
    update_calendar()

def add_event(year, month, day):
    event_date = f"{year}-{month:02}-{day:02}"
    event = simpledialog.askstring("Add Event", f"Enter event for {event_date}:")
    if event:
        events.setdefault(event_date, []).append(event)  # Add event to the date
        update_calendar()  # Refresh calendar display

# Set up main window
root = tk.Tk()
root.title("Interactive Calendar Program with Events")
root.geometry("500x500")

# Make the main window resizable
root.rowconfigure(1, weight=1)  # Row containing the calendar
root.columnconfigure(0, weight=1)

# Year and Month input fields with dropdowns
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, pady=10)

# Previous and Next month buttons
prev_button = tk.Button(input_frame, text="<< Previous Month", command=previous_month)
prev_button.grid(row=0, column=0, padx=5)

next_button = tk.Button(input_frame, text="Next Month >>", command=next_month)
next_button.grid(row=0, column=7, padx=5)

# Month dropdown (combobox)
month_names = list(calendar.month_name)[1:]  # List of month names
tk.Label(input_frame, text="Month:", font=("Arial", 10)).grid(row=0, column=1, padx=5)
month_combobox = ttk.Combobox(input_frame, values=month_names, width=10)
month_combobox.grid(row=0, column=2, padx=5)
month_combobox.set("November")  # Set default month
month_combobox.bind("<<ComboboxSelected>>", on_month_change)  # Update when changed

# Year dropdown (combobox)
tk.Label(input_frame, text="Year:", font=("Arial", 10)).grid(row=0, column=3, padx=5)
years = list(range(1900, 2101))  # Range of years to choose from
year_combobox = ttk.Combobox(input_frame, values=years, width=5)
year_combobox.grid(row=0, column=4, padx=5)
year_combobox.set(2024)  # Set default year
year_combobox.bind("<<ComboboxSelected>>", on_year_change)  # Update when changed

# Frame to display the calendar
calendar_frame = tk.Frame(root)
calendar_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Show initial calendar
show_calendar(2024, 11)

# Start the Tkinter event loop
root.mainloop()
