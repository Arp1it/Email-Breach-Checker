# Email Leak Checker (Flask App)

This is a basic Flask web application that checks if an email address has been involved in any data breaches using the LeakCheck public API.

## Features

* Accepts an email address via a query parameter.
* Uses the LeakCheck API to verify if the email is found in any data breaches.
* Displays the result using a Jinja2 HTML template (`base.html`).

## Requirements

* Python 3.x
* Flask
* requests

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Arp1it/Email-Breach-Checker
cd email-leak-checker
```

2. Install dependencies:

```bash
pip install Flask requests
```

## Usage

Run the Flask app:

```bash
python main.py
```

Visit http://127.0.0.1:5000 in your browser.

To check an email, use a query string like:

```
http://127.0.0.1:5000/?email=example@example.com
```

## File Structure

```
.
├── main.py           # Main Flask application
├── templates/
│   └── base.html    # HTML template to display results
└── README.md        # This file
```

## Notes

* The app uses the public endpoint of LeakCheck. No API key is required.
* Ensure you have an internet connection when using the app.
