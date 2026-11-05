# Secure HTTP Server

## Project Overview
A beginner cybersecurity project built using Python.
It demonstrates how HTTP security headers can improve
the security of a web server.

## Technologies Used
- Python 3
- HTTP Server
- Linux (Ubuntu)

## Security Features
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- Referrer-Policy: no-referrer
- Content-Security-Policy: default-src 'self'

## Installation
Ensure Python 3 is installed.

## How to Run
python3 secure_server.py

The server runs locally at:
http://127.0.0.1:8001

## Testing
Run the following command in another terminal:

curl -I http://127.0.0.1:8001

Verify that the server returns HTTP 200 OK
and all four configured security headers.

## Learning Outcomes
- Understanding HTTP response headers
- Implementing basic web security controls
- Running a local Python HTTP server
- Testing server responses using curl

## Disclaimer
This project is for educational and authorized
local testing purposes only.
It is not intended for production deployment.
