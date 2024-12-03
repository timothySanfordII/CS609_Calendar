import requests

API_KEY = 'N8UYALLyNbsAFVw6BuV67HrogloGQrzs'
LOCATION = 'US'

holiday_data = {}
def get_holidays_for_month(year, month):
    """Fetch holidays data for the specified year and month."""
    global holiday_data

    month_str = f"{month:02d}"
    year_str = str(year)

    if f"{year_str}-{month_str}" in holiday_data:
        return holiday_data[f"{year_str}-{month_str}"]

    try:
        url = f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country={LOCATION}&year={year}&month={month}"
        response = requests.get(url)
        response.raise_for_status()

        holidays = response.json().get('response', {}).get('holidays', [])
        

        # Save name and date, ensuring only one holiday per date (the first one)
        holidays_dict = {}
        for holiday in holidays:
            date = holiday['date']['iso']
            name = holiday['name']
            if date not in holidays_dict:  # Add only if the date is not already in the dictionary
                holidays_dict[date] = name

        # Convert the dictionary to a list of dictionaries
        holidays_list = [{'name': name, 'date': date} for date, name in holidays_dict.items()]
        holiday_data[f"{year_str}-{month_str}"] = holidays_list
        

        return holidays_list
    except requests.RequestException as e:
        print(f"Error fetching holidays: {e}")
        return []
