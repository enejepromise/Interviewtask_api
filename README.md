## Vector Interview API

This project is part of my internship challenge task assigned by MentorLed. It involves building an asynchronous video interview platform using Django and PostgreSQL. The project focuses on implementing an API for creating interview sessions and managing interview data efficiently.

Tasks Overview

## Task 2: Create Interview API

Core Focus: Implementing a REST API for creating an interview session with fields (title, description, questions). Store interview data in PostgreSQL.

To enable recruiters to create and manage interview sessions, I implemented an API that allows the creation of interview sessions with essential details such as title, description, and questions. This ensures that interview sessions are properly structured and stored in the database for further retrieval.

## Steps Implemented:

1. Setting up Django and PostgreSQL – Installed Django, Django REST framework (DRF), and PostgreSQL dependencies to set up the development environment.

2. Activated virtual machine

3. Created Interview Model –I Defined the model with title, description, and questions fields to represent an interview session in the database.

4. Implemented Serializer – I used Django REST framework’s serializer to convert model instances into JSON format for API responses, ensuring seamless data exchange between the backend and frontend.

5. Developed Views & Endpoints – I created API views using Django REST framework to handle interview creation and store data in PostgreSQL.

6.Configured URLs – Added an interview creation endpoint to Django’s URL patterns, making it accessible via API calls.

Tested API – Used the Django admin panel to send POST requests and verify successful interview creation and data storage.

## Task 3: Fetching & Managing Interviews

Core Focus: Implement API endpoints to fetch all interviews and get interview details by ID, including pagination.

To make the interview process more efficient, I implemented API endpoints that allow recruiters and evaluators to fetch all interviews, retrieve details of a specific interview by ID, and handle large datasets efficiently through pagination.

Steps Implemented:

Created Fetch Endpoints – Implemented API views to retrieve all interview records and fetch details of a specific interview by ID.

Implemented Pagination – Added pagination support to manage large interview datasets efficiently, preventing overload and ensuring smooth API responses.

Updated Serializer – Ensured that the retrieved interview data is properly formatted and structured for easy consumption by frontend applications.

Configured URLs – Added interview retrieval endpoints to Django’s URL patterns to make them accessible.

Tested API – Used Postman to confirm successful retrieval of interviews, test pagination, and verify data accuracy.

Technologies Used

Django & Django REST Framework – Backend development and API implementation.

PostgreSQL – Database for storing interview data.

Postman – API testing to ensure functionality.
