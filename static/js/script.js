/* ------------------------------ Handles the form submission via AJAX and displays a popup */

console.log('JavaScript is loaded and running.');

// Wait until the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Select the form element using its ID
    const form = document.querySelector('#newsletter-subscription-form');
    
    // Add an event listener to handle form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Create a FormData object from the form
        const formData = new FormData(form);

        // Send the form data via Fetch API
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': form.querySelector('input[name="csrfmiddlewaretoken"]').value
            }
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            if (data.success) {
                // Show success message if the submission was successful
                alert('Subscription successful!');
            } else {
                // Handle errors if submission failed
                const modalBodyContent = document.getElementById('modal-body-content');
                modalBodyContent.innerHTML = ''; // Clear previous error messages
                
                if (data.errors) {
                    // Create an unordered list to display errors
                    const errorList = document.createElement('ul');
                    for (const field in data.errors) {
                        if (data.errors.hasOwnProperty(field)) { // Ensure we only process direct properties
                            data.errors[field].forEach(error => {
                                const listItem = document.createElement('li');
                                listItem.textContent = `${field}: ${error}`;
                                errorList.appendChild(listItem);
                            });
                        }
                    }
                    modalBodyContent.appendChild(errorList);
                }

                // Initialise and show the error modal
                const errorModal = new bootstrap.Modal(document.getElementById('errorModal'), {
                    backdrop: 'static', // Disable closing by clicking outside the modal
                    keyboard: true // Enable closing with the Esc key
                });
                errorModal.show();
            }
        })
        .catch(error => {
            console.error('Error:', error); // Log any errors encountered during fetch
        });
    });
});


/* ---------------------------------- Footer link modal to external page */

document.addEventListener('DOMContentLoaded', function() {
    // Select the modal and buttons
    const modal = document.getElementById("footer-link-modal");
    const btn = document.getElementById("external-link");
    const span = document.getElementsByClassName("close")[0];
    const acceptBtn = document.getElementById("accept");
    const declineBtn = document.getElementById("decline");

    // Define the URL to open when the "Accept" button is clicked
    const externalURL = "https://portal.aestheticnursesoftware.com/book-online/8300";
    let lastFocusedElement;

    // Open the modal when the external link button is clicked
    btn.onclick = function(event) {
        event.preventDefault(); // Prevent the default action of the link
        lastFocusedElement = document.activeElement; // Store the last focused element
        modal.style.display = "block"; // Show the modal
        acceptBtn.focus(); // Move focus to the "Accept" button
    };

    // Close the modal when the "x" span is clicked
    span.onclick = function() {
        closeModal();
    };

    // Redirect to the external URL when the "Accept" button is clicked
    acceptBtn.onclick = function() {
        window.open(externalURL, '_blank'); // Open the URL in a new tab
        closeModal();
    };

    // Close the modal when the "Decline" button is clicked
    declineBtn.onclick = function() {
        closeModal();
    };

    // Close the modal if clicking outside of it
    window.onclick = function(event) {
        if (event.target === modal) { // Use strict equality for comparison
            closeModal();
        }
    };

    // Function to close the modal and return focus to the last focused element
    function closeModal() {
        modal.style.display = "none"; // Hide the modal
        if (lastFocusedElement) {
            lastFocusedElement.focus(); // Return focus to the last focused element
        }
    }

    // Close the modal when the Escape key is pressed
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && modal.style.display === "block") {
            closeModal();
        }
    });
});

// Initialise the carousel on document ready
$(document).ready(function() {
    $('#home-carousel').carousel({
        interval: 3000, // Time between slides (3 seconds)
        wrap: true // Enable infinite looping of slides
    });
});

// Prevent default behavior for carousel control buttons
$('.carousel-control-prev, .carousel-control-next').click(function(event) {
    event.preventDefault(); // Prevent the default action
});
