document.addEventListener('DOMContentLoaded', function() {
    const calendar = document.getElementById('calendar');
    const eventModal = document.getElementById('event-modal');
    const eventInput = document.getElementById('event-input');
    const saveButton = document.getElementById('save-event');
    const closeButton = document.getElementById('close-modal');
    const monthSelect = document.getElementById('month-select');
    const yearSelect = document.getElementById('year-select');
    let selectedDate = '';
    let currentDate = new Date();

    const createCalendar = async () => {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        const months = ["January", "February", "March", "April", "May", "June", 
                        "July", "August", "September", "October", "November", "December"];
        
        monthSelect.innerHTML = '';
        months.forEach((monthName, index) => {
            const option = document.createElement('option');
            option.value = index;
            option.textContent = monthName;
            if (index === month) option.selected = true;
            monthSelect.appendChild(option);
        });

        yearSelect.innerHTML = '';
        for (let y = year - 5; y <= year + 5; y++) {
            const option = document.createElement('option');
            option.value = y;
            option.textContent = y;
            if (y === year) option.selected = true;
            yearSelect.appendChild(option);
        }

        const firstDay = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        calendar.innerHTML = '';
        for (let i = 0; i < firstDay; i++) {
            const emptyCell = document.createElement('div');
            emptyCell.className = 'empty-cell';
            calendar.appendChild(emptyCell);
        }

        for (let day = 1; day <= daysInMonth; day++) {
            const dayContainer = document.createElement('div');
            dayContainer.className = 'day-container';

            const dayElement = document.createElement('div');
            dayElement.textContent = day;
            dayElement.className = 'day';
            const formattedDate = `${year}-${month + 1}-${day < 10 ? '0' + day : day}`; // Format date

            if (day === currentDate.getDate() && month === currentDate.getMonth() && year === currentDate.getFullYear()) {
                dayElement.classList.add('current-day'); // Highlight current day
            }

            dayElement.onclick = async () => {
                selectedDate = formattedDate;
                eventModal.style.display = 'block';
                await loadEvents(formattedDate);
            };

            dayContainer.appendChild(dayElement);
            calendar.appendChild(dayContainer);
        }
    };

    const loadEvents = async (date) => {
        const events = await fetch(`/events/${date}`).then(res => res.json());
        const eventList = document.getElementById('event-list');
        eventList.innerHTML = ''; // Clear existing events
        if (events.events.length === 0) {
            eventList.innerHTML = '<p>No events for this date.</p>';
        } else {
            events.events.forEach(event => {
                const listItem = document.createElement('div');
                listItem.textContent = event.name;
                listItem.className = 'event-item';

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.className = 'delete-button';
                deleteButton.onclick = async (e) => {
                    e.stopPropagation(); // Prevent modal close
                    await deleteEvent(event.id);
                    loadEvents(selectedDate); // Refresh the event list
                };

                listItem.appendChild(deleteButton);
                eventList.appendChild(listItem);
            });
        }
    };

    const saveEvent = () => {
        const eventName = eventInput.value.trim();

        if (!eventName) {
            alert('Please enter an event name.');
            return;
        }

        fetch(`/events/${selectedDate}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ event: eventName })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Event saved!');
                eventInput.value = '';
                loadEvents(selectedDate); // Refresh the event list for the selected date
            } else {
                alert(`Error: ${data.message}`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error saving the event. Please try again.');
        });
    };

    const deleteEvent = async (eventId) => {
        await fetch(`/delete-event/${eventId}`, {
            method: 'DELETE'
        });
        alert('Event deleted!');
    };

    saveButton.onclick = saveEvent;

    closeButton.onclick = () => {
        eventModal.style.display = 'none';
    };

    window.onclick = function(event) {
        if (event.target == eventModal) {
            eventModal.style.display = 'none';
        }
    };

    monthSelect.onchange = () => {
        currentDate.setMonth(monthSelect.value);
        createCalendar();
    };

    yearSelect.onchange = () => {
        currentDate.setFullYear(yearSelect.value);
        createCalendar();
    };

    createCalendar();
});
