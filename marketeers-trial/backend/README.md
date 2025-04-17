# Flask Backend for MarketEers Trial

This repository contains the backend code for the MarketEers Trial project. It is built using **Flask** as the web framework and exposes REST APIs for frontend communication.

---

## Project Setup

Follow these steps to set up and run the backend:

### 1. **Clone the Repository**

Clone this repository to your local machine:

git clone <repository_url>
cd <repository_name>


Make sure you have pip installed and run:

pip install -r requirements.txt
This will install all the required libraries for the backend, including Flask and any other necessary dependencies.

4. Setup Environment Variables
Create a .env file in the root of the project to define environment variables, such as database credentials and secret keys. Here is an example .env file:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
DATABASE_URI=your_database_uri_here



5. Run the Backend Server
To start the Flask development server, use the following command:


python app.py
By default, the Flask app will run on http://127.0.0.1:5000/.

You can also specify a different host and port by running:

flask run --host=0.0.0.0 --port=your_port
6. Test the API
Once the Flask server is running, you can test the API endpoints using Postman or cURL.

The basic API endpoints are:

Login Endpoint (POST /api/login): Accepts user credentials and returns a JWT token.

Data Endpoint (GET /api/data): A sample API to fetch data from the database.

7. JWT Authentication
To use the authentication system, you need to first log in to get a JWT token. The token will be required for accessing protected routes.

Login Credentials
For testing purposes, the login credentials are:

Username: admin

Password: admin

Example: Login Request
Send a POST request to /api/login with the following JSON body:

{
  "username": "admin",
  "password": "admin"
}
If successful, the response will include a token:

{
  "access_token": "your_jwt_token_here"
}
You can then pass this token in the Authorization header as a Bearer token for future API calls.

API Documentation
Login
URL: /api/login

Method: POST

Request Body:

{
  "username": "admin",
  "password": "admin"
}
Response:

{
  "access_token": "your_jwt_token_here"
}
Sample Data
URL: /api/data

Method: GET

Authorization: Bearer JWT token required.

Response:

[
  {
    "id": 1,
    "name": "Sample Data 1",
    "value": 100
  },
  {
    "id": 2,
    "name": "Sample Data 2",
    "value": 200
  }
]
Libraries Used
Flask: A lightweight Python web framework for building APIs.

Flask-JWT-Extended: For JWT authentication and token management.

Flask-SQLAlchemy: For interacting with the database.

Flask-Migrate: For database migrations.

Contributing
Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Create a new Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.


### Key Updates:
- Added a section under **JWT Authentication** specifying that for login, the **username** and **password** are both `admin`.







