/* ------------------------------ Handles the form submission via AJAX and displays a popup */

console.log('JavaScript is loaded and running.');

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('newsletter-form');
    const errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
    const modalBodyContent = document.getElementById('modal-body-content');

    console.log('JavaScript loaded and running.');

    if (form) {
        console.log('Form found:', form);

        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting normally

            console.log('Form submitted');
            
            const formData = new FormData(form);

            console.log('Form data:', [...formData.entries()]);

            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
                }
            })
            .then(response => {
                console.log('Response status:', response.status);
                return response.json();
            })
            .then(data => {
                console.log('Response data:', data);

                if (data.success) {
                    alert('Subscription successful!');
                    form.reset(); // Optionally clear the form
                } else {
                    modalBodyContent.innerHTML = ''; // Clear any previous content
                    if (data.errors) {
                        Object.keys(data.errors).forEach(key => {
                            data.errors[key].forEach(error => {
                                modalBodyContent.innerHTML += `<p>${error}</p>`;
                            });
                        });
                    }
                    errorModal.show(); // Show the modal
                }
            })
            .catch(error => {
                console.error('Error during fetch:', error);
                modalBodyContent.innerHTML = `<p>Something went wrong. Please try again later.</p>`;
                errorModal.show(); // Show the modal
            });
        });
    } else {
        console.error('Form element not found.');
    }
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