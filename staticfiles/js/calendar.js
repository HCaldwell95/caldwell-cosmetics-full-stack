// calendar.js

document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    
    // Create a new FullCalendar instance
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // Initial view as a monthly grid
        events: function(fetchInfo, successCallback, failureCallback) {
            fetch('/booking_events/')  // URL of your user bookings endpoint
                .then(response => response.json())
                .then(data => successCallback(data))  // Pass the fetched events to FullCalendar
                .catch(error => failureCallback(error));  // Handle errors if necessary
        }
    });
    
    // Render the calendar
    calendar.render();
});
