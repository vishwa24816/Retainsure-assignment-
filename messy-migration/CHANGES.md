# Changelog

## Major Issues Identified

- **SQL Injection:** The application was vulnerable to SQL injection attacks due to the use of f-strings to build queries.
- **Plain Text Passwords:** Passwords were stored in plain text, which is a major security risk.
- **Lack of Code Organization:** All the code was in a single file, making it difficult to maintain and understand.
- **Inconsistent API Responses:** The API returned a mix of plain text and JSON, and used improper HTTP status codes.
- **No Input Validation:** The application did not validate user input, which could lead to errors and security vulnerabilities.
- **Improper Database Connection Management:** The application used a single global database connection, which is not a good practice.

## Changes Made in The Code

- **Project Structure:** The project was restructured into a more modular and maintainable format.
  - `src/app.py`: Initializes the Flask application.
  - `src/database.py`: Handles all database interactions.
  - `src/routes.py`: Defines all the API routes.
  - `src/utils.py`: Contains utility functions, such as password hashing.
  - `tests/`: Contains all the tests for the application.
- **Security:**
  - **SQL Injection Prevention:** All SQL queries now use parameterized statements to prevent SQL injection.
  - **Password Hashing:** Passwords are now hashed using `bcrypt` before being stored in the database.
- **API Improvements:**
  - **JSON Responses:** All API endpoints now return JSON responses.
  - **HTTP Status Codes:** The API now uses appropriate HTTP status codes to indicate the status of a request.
- **Input Validation:** Basic input validation has been added to all endpoints that accept data.
- **Database Connection Management:** The application now uses a connection pool to manage database connections, and connections are closed after each query.
 **Frontend Added:** A simple HTML frontend (`src/frontend.html`) was added to allow easy testing of user management endpoints (fetch users, create user, login) via browser.
 **Import Fixes:** Python import statements were updated to allow the backend to run directly from the `src` directory, resolving relative import errors.
 **Verified Endpoints:** All user management endpoints (CRUD, search, login) were verified to work with both API clients and the new frontend.
## Assumptions and Trade-offs

- I assumed that the application would be deployed in a containerized environment, so I did not add any environment-specific configuration.
 - The frontend is a minimal HTML file for demonstration and basic testing; it is not styled for production use.
 - The backend is designed to run locally for development and testing. For deployment, further configuration (such as environment variables and production server setup) would be needed.
 - No advanced frontend frameworks were used to keep the solution simple and easy to maintain.
 - No new business features were added beyond those required for user management and security improvements.

