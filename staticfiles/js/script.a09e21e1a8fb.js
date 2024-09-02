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