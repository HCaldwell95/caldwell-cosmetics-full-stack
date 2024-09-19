document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    
    // Create a new FullCalendar instance
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // Initial view as a monthly grid
        events: function(fetchInfo, successCallback, failureCallback) {
            fetch('/events/')  // Use the URL of your booking events endpoint
                .then(response => response.json())
                .then(data => {
                    successCallback(data);  // Pass the fetched events to FullCalendar
                })
                .catch(error => {
                    console.error('Error fetching events:', error);
                    failureCallback(error);  // Handle errors if necessary
                });
        }
    });
    
    // Render the calendar
    calendar.render();
});
