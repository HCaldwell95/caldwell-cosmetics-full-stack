/* ------------------------------ Handles the form submission via AJAX and displays a popup */

console.log('JavaScript is loaded and running.');

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#newsletter-subscription-form');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': form.querySelector('input[name="csrfmiddlewaretoken"]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Optionally, you can show a success message or redirect
                alert('Subscription successful!');
            } else {
                // If there are errors, display them in the modal
                const modalBodyContent = document.getElementById('modal-body-content');
                modalBodyContent.innerHTML = ''; // Clear previous errors
                
                if (data.errors) {
                    const errorList = document.createElement('ul');
                    for (let field in data.errors) {
                        data.errors[field].forEach(error => {
                            const listItem = document.createElement('li');
                            listItem.textContent = ${field}: ${error};
                            errorList.appendChild(listItem);
                        });
                    }
                    modalBodyContent.appendChild(errorList);
                }

                // Show the modal
                const errorModal = new bootstrap.Modal(document.getElementById('errorModal'), {
                    backdrop: 'static', // Disables closing by clicking outside the modal
                    keyboard: true // Enables closing with the Esc key
                });
                errorModal.show();
                
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});


/* ---------------------------------- Footer link modal to external page */

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById("footer-link-modal");
    const btn = document.getElementById("external-link");
    const span = document.getElementsByClassName("close")[0];
    const acceptBtn = document.getElementById("accept");
    const declineBtn = document.getElementById("decline");

    const externalURL = "https://portal.aestheticnursesoftware.com/book-online/8300";
    let lastFocusedElement;

    // When the user clicks the link, open the modal
    btn.onclick = function(event) {
        event.preventDefault();
        lastFocusedElement = document.activeElement; // Store the last focused element
        modal.style.display = "block";
        acceptBtn.focus(); // Move focus to the first actionable element in the modal
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        closeModal();
    }

    // When the user clicks the "Accept" button, redirect to the external site
    acceptBtn.onclick = function() {
        window.open(externalURL, '_blank');
        closeModal();
    }

    // When the user clicks the "Decline" button, close the modal
    declineBtn.onclick = function() {
        closeModal();
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            closeModal();
        }
    }

    // Close the modal and return focus to the triggering element
    function closeModal() {
        modal.style.display = "none";
        if (lastFocusedElement) {
            lastFocusedElement.focus(); // Return focus to the last focused element
        }
    }

    // Close the modal when pressing the Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && modal.style.display === "block") {
            closeModal();
        }
    });
});

// Carousel JS 
$(document).ready(function() {
    $('#home-carousel').carousel({
        interval: 3000, // Time between slides
        wrap: true // Infinite loop
    });
});

$('.carousel-control-prev, .carousel-control-next').click(function(event) {
    event.preventDefault();
});