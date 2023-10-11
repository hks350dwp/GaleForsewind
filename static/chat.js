function sendMessage() {
    var userInput = document.getElementById('userInput').value;
    appendMessage('User: ' + userInput, 'user');

    fetch('/chatbot/', {  // This should be the URL pattern of your Django view
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Handle CSRF token if CSRF protection is enabled
        },
        body: JSON.stringify({text: userInput})  // Send user input as JSON to Django
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('Bot: ' + data.response, 'bot');  // Handle the response from Django
    })
    .catch(error => console.error('Error during fetch operation: ', error));
}

function appendMessage(message, sender) {
    var chatbox = document.getElementById('chatbox');
    var messageDiv = document.createElement('div');
    messageDiv.className = sender;
    messageDiv.innerText = message;
    chatbox.appendChild(messageDiv);
}
