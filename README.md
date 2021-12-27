URL Shortener Application
=========================

# Overview: 
A URL Shortener application

Users can input a valid HTTP/HTTPS URL into the React form and expect a shortened URL. This application
runs on the Nginx webserver (localhost:8080).

The front-end is written in React and is running on the Nginx webserver.
The back-end REST API is written in Python and Flask. 
The database used is MongoDB, which is controlled through the REST API.

![Diagram](URLShortenerDiagram.png)

# Running the application:
The application will be executed through Docker/docker-compose.

## Instructions for running the program:
1. Download the source code and go to the root directory of the project
2. (Make sure to have Docker installed!) Run the command **docker-compose -f docker-compose.yml up --build**. That's it! Everything should be running.
3. To turn off the application, run the command **docker-compose -f docker-compose.yml down -v**

# Testing:
By default, all tests should run after executing the docker-compose command in step two of running the application.
If you want manually unit test each service, the instructions are below.

## Instructions for testing the React Application:
1. Go to the project directory
2. (Make sure to have npm installed!) Run the command **npm test**

## Instructions for testing the API:
1. Navigate to the **url-shortener-api** directory
2. Run the command **python3 test_cases.python3**

# MongoDB Table:
The database and the collection are automatically created through docker-compose and the REST API.
Each document in the table has three attributes: '_id', 'original_url', and 'slug'.
- (e.g.) {"_id":{"$oid":"61c2394f2988b5c32a99e37e"},"original_url":"http://127.0.0.1:5000/","slug":"5ac637"}

# Endpoints:
- React/Nginx: 8080
- Python/Flask API: 5001
- MongoDB: 27017
- Collection name: url-shortener-db
- Username: mongodb
- Password: mongodb
