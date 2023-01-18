
 # CV in Flask
 
    This is a Python application that allows users to view CV data in a web page and as a JSON object. 
    The application is built using Flask and it has an API endpoints which returns CV data in a JSON format.
    It also allows users to process the CV data and returns a formatted string. 

Requirements

    Python 3.x
    Flask
    Click
    Blueprints
    Logging
    Typing

Installation

    Clone the repository
    Install the required libraries using pip
    Start the application using flask run command

Usage

    The application has a main file app.py which starts the Flask application, and it has two other files blueprints.py 
    and services/process_cv_data.py containing the routes and the functions to process the CV data respectively.

Input

    static/cv_data.py : dict
    A dictionary with CV data in a specific format, see static/cv_data.py for details.

Output

    http://localhost:5000/endpoint : json
    A json containing the information at the endpoint.

    flask print_cv : string
    A formatted string with all the data from the CV.

CLI Command

    To execute the CLI command, run 'flask print_cv' in the command line.

API Endpoints

    /personal - Returns the personal data from the cv_data.py file
    /competencies - Returns the core competencies from the cv_data.py file
    /experience - Returns the professional experience from the cv_data.py file
    /projects - Returns the personal projects from the cv_data.py file
    /education - Returns the education data from the cv_data.py file

Access endpoints in browser

    To access endpoints in browser:

    1. Run the application by executing python app.py
    2. The API should now be running on http://localhost:5000/
    3. Access the endpoints above. (e.g. http://localhost:5000/personal)

Logging

    The module uses the built-in Python logging module to log any errors that occur while processing the data. 
    The logs can be accessed by the user to troubleshoot any issues.

License

    This project is licensed under the MIT License.