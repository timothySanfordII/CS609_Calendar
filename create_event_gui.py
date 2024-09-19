import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x400")

# List to store event details
events = []

# Initialize event number counter
event_counter = 1

def create_event():
    global event_counter  # Use the global event_counter to keep track of event numbers
    name = entry_name.get()
    day = entry_day.get()
    month = entry_month.get()
    year = entry_year.get()

    # Store the event details in a dictionary and append to the events list
    event_details = {
        "event_number": event_counter,
        "name": name,
        "day": day,
        "month": month,
        "year": year
    }
    events.append(event_details)
    
    # Print all stored events
    print(f"Stored Events: {events}")
    
    # Increment event_counter for the next event
    event_counter += 1

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Create Event", font=("Roboto", 24))
label.pack(pady=12, padx=10)

# Input box for name of event
entry_name = customtkinter.CTkEntry(master=frame, placeholder_text="Event Name")
entry_name.pack(pady=12, padx=10)

# Input box for day
entry_day = customtkinter.CTkEntry(master=frame, placeholder_text="Day (DD)")
entry_day.pack(pady=12, padx=10)

# Input box for month
entry_month = customtkinter.CTkEntry(master=frame, placeholder_text="Month (MM)")
entry_month.pack(pady=12, padx=10)

# Input box for year
entry_year = customtkinter.CTkEntry(master=frame, placeholder_text="Year (YYYY)")
entry_year.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Enter", command=create_event)
button.pack(pady=12, padx=10)

root.mainloop()
