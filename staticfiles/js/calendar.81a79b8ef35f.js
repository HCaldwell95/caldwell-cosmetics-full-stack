document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');

    if (calendarEl) {  // Ensure the element exists
        // Create a new FullCalendar instance
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth', // Initial view as a monthly grid
            events: function(fetchInfo, successCallback, failureCallback) {
                fetch('/booking_events/')  // URL of your user bookings endpoint
                    .then(response => response.json())
                    .then(data => {
                        if (Array.isArray(data)) {
                            successCallback(data);  // Pass the fetched events to FullCalendar
                        } else {
                            console.error('Invalid data format:', data);
                            failureCallback('Invalid data format');
                        }
                    })
                    .catch(error => {
                        console.error('Error fetching events:', error);
                        failureCallback(error);  // Handle errors if necessary
                    });
            }
        });

        // Render the calendar
        calendar.render();
    } else {
        console.error('Calendar element not found');
    }
});