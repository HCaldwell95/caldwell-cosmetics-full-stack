$(document).ready(function() {
    $('#calendar').fullCalendar({
        events: '/path/to/your/appointments/',  // URL to fetch appointments
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    
    // Create a new FullCalendar instance
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // Initial view as a monthly grid
        events: [
            { title: 'Meeting', start: new Date().toISOString().split('T')[0] } // Example event
        ]
    });
    
    // Render the calendar
    calendar.render();
});
