# Project Documentation – Factorial Web App

## Overview

This project is a basic web application that calculates the factorial of a number using a Flask backend. It demonstrates how backend logic, templates, and frontend assets work together in a web application.



## Backend (app.py)

### Flask App Initialization

* A Flask application instance is created.
* Routes are defined to handle HTTP requests.

### factorial() Function

* Accepts an integer input
* Returns:

  * Factorial value for valid inputs
  * -1 for negative numbers
  * Raises TypeError for invalid types

### Routing

#### `/` Route

* Supports both GET and POST methods
* GET → renders the page
* POST → processes user input

### Error Handling

* ValueError → invalid input (non-integer)
* TypeError → incorrect data type
* Custom message for negative numbers



## Frontend

### HTML (index.html)

* Form to accept user input
* Displays:

  * Result
  * Error messages
* Uses Jinja2 templating

### CSS (style.css)

* Black background with yellow container
* Responsive design
* Smooth animations
* Styled buttons and input fields

### JavaScript (script.js)

#### Features:

* Loading spinner on form submit
* Client-side validation (checks if input is number)
* Copy-to-clipboard functionality



## Data Flow

1. User enters a number
2. Form sends POST request
3. Flask processes input
4. Result/error sent to template
5. UI updates dynamically



## Key Design Decisions

* Used Flask for simplicity and learning backend basics
* Kept UI minimal for clarity
* Added both client-side and server-side validation



## Limitations

* Cannot handle extremely large numbers efficiently
* No database or persistent storage
* No API endpoints (only web interface)



## Conclusion

This project serves as a foundational example of building a full-stack web application using Python Flask and basic frontend technologies.
