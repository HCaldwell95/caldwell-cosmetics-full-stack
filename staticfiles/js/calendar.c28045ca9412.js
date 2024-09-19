import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';  // For interaction events

document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');

    // Create a new FullCalendar instance
    const calendar = new Calendar(calendarEl, {
        plugins: [dayGridPlugin, interactionPlugin],  // Use necessary plugins
        initialView: 'dayGridMonth',  // Initial view as a monthly grid
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
        },
        dateClick: function(info) {
            alert('Clicked on: ' + info.dateStr);
            alert('Coordinates: ' + info.jsEvent.pageX + ',' + info.jsEvent.pageY);
            alert('Current view: ' + info.view.type);
            // change the day's background color just for fun
            info.dayEl.style.backgroundColor = 'red';
        }
    });

    // Render the calendar
    calendar.render();
});
