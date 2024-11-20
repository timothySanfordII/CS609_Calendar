import requests

def fetch_holidays(country, year, api_key):
    url = f"https://date.nager.at/api/v2/publicholidays/{year}/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        holidays = response.json()
        return holidays
    else:
        print("Failed to fetch holiday data")
        return []

def display_holidays(holidays):
    print("Upcoming Holidays:")
    for holiday in holidays:
        print(f"{holiday['date']}: {holiday['localName']}")

if __name__ == "__main__":
    country = "US"  # Change this to the desired country code
    year = 2024
    api_key = "YOUR_API_KEY"  # Not required for Nager.Date, but needed for Calendarific
    holidays = fetch_holidays(country, year, api_key)
    display_holidays(holidays)
