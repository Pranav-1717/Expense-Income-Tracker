document.addEventListener('DOMContentLoaded', function() {
    var closeButtons = document.querySelectorAll('.alert .close');
    closeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var alert = this.closest('.alert');
            alert.style.display = 'none'; // or use a CSS class to hide it
        });
    });

    // Function to automatically close the alert after a specified duration
    function closeAlertAfter(alert, duration) {
        setTimeout(function() {
            alert.style.display = 'none'; // or use a CSS class to hide it
        }, duration);
    }

    // Usage example: Close alerts after 5 seconds
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        closeAlertAfter(alert, 1000); // 5000 milliseconds = 5 seconds
    });
});


