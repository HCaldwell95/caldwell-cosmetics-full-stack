document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');

    if (calendarEl) {
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            validRange: {
                start: new Date().toISOString().split('T')[0]  // prevent selecting past dates
            },
            events: function(fetchInfo, successCallback, failureCallback) {
                fetch('/bookings/booking_events/')  // Absolute path here
                    .then(response => response.json())
                    .then(data => {
                        if (Array.isArray(data)) {
                            successCallback(data);
                        } else {
                            console.error('Invalid data format:', data);
                            failureCallback('Invalid data format');
                        }
                    })
                    .catch(error => {
                        console.error('Error fetching events:', error);
                        failureCallback(error);
                    });
            },
            eventTimeFormat: {   // <-- Add this
                hour: 'numeric',
                minute: '2-digit',
                meridiem: 'short'  // shows full 'am' or 'pm'
            }
        });

        calendar.render();
    } else {
        console.error('Calendar element not found');
    }
});
