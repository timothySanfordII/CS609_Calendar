from flask import Flask, request, jsonify
import customtkinter

app = Flask(__name__)

# List to store event details
events = []
event_counter = 1

def create_event(name, day, month, year):
    global event_counter
    event_details = {
        "event_number": event_counter,
        "name": name,
        "day": day,
        "month": month,
        "year": year
    }
    events.append(event_details)
    event_counter += 1
    return event_details

@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.get_json()
    event_name = data.get('name')
    event_day = data.get('day')
    event_month = data.get('month')
    event_year = data.get('year')
    
    event = create_event(event_name, event_day, event_month, event_year)
    
    return jsonify({"message": f"Event {event['name']} added!"})

if __name__ == '__main__':
    app.run(debug=True)
