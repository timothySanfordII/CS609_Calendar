from flask import Flask, render_template
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Get current year and month
    year = datetime.now().year
    month = datetime.now().month
    
    # Create a calendar
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    cal_html = cal.formatmonth(year, month)
    
    return render_template('calendar.html', calendar=cal_html)

if __name__ == '__main__':
    app.run(debug=True)
