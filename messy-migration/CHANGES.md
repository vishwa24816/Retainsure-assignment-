# Changelog

## Major Issues Identified 

- **SQL Injection Vulnerability:** The application was vulnerable to SQL injection attacks due to the use of f-strings to build queries.
- **Plain Text Passwords:** Passwords were stored in plain text, which is a major security risk.
- **Lack of Code Organization:** All the code was in a single file, making it difficult to maintain and understand.
- **Inconsistent API Responses:** The API returned a mix of plain text and JSON, and used improper HTTP status codes.
- **No Input Validation:** The application did not validate user input, which could lead to errors and security vulnerabilities.
- **Improper Database Connection Management:** The application used a single global database connection, which is not a good practice.

## Changes made to Rectify the same

- **Project Structure is updated:** The project was restructured into a more modular and maintainable format.
  - `src/app.py`: Initializes the Flask application.
  - `src/database.py`: Handles all database interactions.
  - `src/routes.py`: Defines all the API routes.
  - `src/utils.py`: Contains utility functions, such as password hashing.
  - `tests/`: Contains all the tests for the application.
- **Security:**
  - **SQL Parameterized:** All SQL queries now use parameterized statements to prevent SQL injection.
  - **Password Hashing:** Passwords are now hashed using `bcrypt` before being stored in the database.
- **API Improvements:**
  - **JSON Responses:** All API endpoints now return JSON responses.
  - **HTTP Status Codes:** The API now uses appropriate HTTP status codes to indicate the status of a request.
- **Input Validation:** Basic input validation has been added to all endpoints that accept data.
- **Database Connection Management:** The application now uses a connection pool to manage database connections, and connections are closed after each query.
- **Testing:** A suite of tests has been added to ensure the application is working correctly.

## Assumptions and Trade-offs Made

- I assumed that the application would be deployed in a containerized environment, so I did not add any environment-specific configuration.
- I focused on fixing the most critical issues and did not add any new features.
