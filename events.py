from datetime import datetime
from database import save_event_to_db, update_event_in_db, delete_event_from_db, get_events_for_month

def add_event_logic(event_date, event_description, current_year, current_month):
    event_date_obj = datetime.strptime(event_date, "%Y-%m-%d")
    if event_date_obj.year == current_year and event_date_obj.month == current_month:
        save_event_to_db(event_date, event_description)
        return True
    return False

def edit_event_logic(event_id, new_date, new_description):
    datetime.strptime(new_date, "%Y-%m-%d")  # Validate date
    update_event_in_db(event_id, new_date, new_description)

def delete_event_logic(event_id):
    delete_event_from_db(event_id)
