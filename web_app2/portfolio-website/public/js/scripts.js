document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get user input
    const name = document.getElementById('name').value;

    // Display confirmation message
    const confirmationMessage = `Thank you for contacting us, ${name}! We'll get back to you shortly.`;
    document.getElementById('confirmation-message').textContent = confirmationMessage;

    // Optionally clear form fields
    document.getElementById('contact-form').reset();
});
