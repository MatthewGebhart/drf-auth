# LAB - Class 33
## Project: Django REST Authentication & Production Server
## Author: Matthew Gebhart

## Setup
python 3.11 .venv environment
Deployed to a Docker container

## How to initialize/run your application
- local server 
- docker compose up
## Tests
- testing for the "get tokens" component is done in Thunder Client as outlined below:
  - test url is http://0.0.0.0:8000/api/token/
  - method is POST
  - adding my test account credentials to the JSON to the Body of the request
    - {"username":"my_username", "password":"my_password"
  - Returns with Status: 200 OK and the tokens for both "refresh": and "access":