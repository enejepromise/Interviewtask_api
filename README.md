# Vector Interview API

This project is part of my internship challenge task assigned by MentorLed. It involves building an asynchronous video interview platform using Django and PostgreSQL. The project focuses on implementing an API for creating interview sessions and managing interview data efficiently.

# Tasks Overview

## Task 2: Create Interview API

Core Focus: Implementing a REST API for creating an interview session with fields (title, description, questions). Store interview data in PostgreSQL.

To enable recruiters to create and manage interview sessions, I implemented an API that allows the creation of interview sessions with essential details such as title, description, and questions. This ensures that interview sessions are properly structured and stored in the database for further retrieval.

## Steps Implemented:

   1. Setting up Django and PostgreSQL – Installed Django, Django REST framework (DRF), and PostgreSQL dependencies to set up the development environment.

   2. Activated virtual machine

   3. Created Interview Model –I Defined the model with title, description, and questions fields to represent an interview session in the database.

   4. Implemented Serializer – I used Django REST framework’s serializer to convert model instances into JSON format for API responses, ensuring seamless data exchange between the 
      backend   and frontend.

   5. Developed Views & Endpoints – I created API views using Django REST framework to handle interview creation and store data in PostgreSQL.

   6. Configured URLs – Added an interview creation endpoint to Django’s URL patterns, making it accessible via API calls.

   7. Tested API – Used the Django admin panel to send POST requests and verify successful interview creation and data storage.

# Task 3: Fetching & Managing Interviews

### Core Focus: Implement API endpoints to fetch all interviews and get interview details by ID, including pagination.

### To make the interview process more efficient, I implemented API endpoints that allow recruiters and evaluators to fetch all interviews, retrieve details of a specific interview by   ID, and handle large datasets efficiently through pagination.

## Steps Implemented:

   1. Created Fetch Endpoints – Implemented API views to retrieve all interview records and fetch details of a specific interview by ID.

   2. Implemented Pagination – Added pagination support to manage large interview datasets efficiently, preventing overload and ensuring smooth API responses.

   3. Updated Serializer – Ensured that the retrieved interview data is properly formatted and structured for easy consumption by frontend applications.

   4. Configured URLs – Added interview retrieval endpoints to Django’s URL patterns to make them accessible.

   5. Tested API – Used Curl command on git bash to confirm successful retrieval of interviews by 1d, and tested for pagination

## Technologies Used

   1. Django & Django REST Framework – Backend development and API implementation.

   2. PostgreSQL – Database for storing interview data.

   3. Curl command – API testing to ensure functionality.

## Task 4

### Video Upload API

This project is about implementing a Video Upload API built with Django, using Cloudinary for video storage. This API allows users to upload videos and retrieve them as needed.

## Features
1. Upload videos to Cloudinary.
2. Store video metadata (URL, duration) in the database.
3. Fetch and manage uploaded videos via API endpoints.
4. Secure authentication for API access.
5. Tested API – Used Postman to check the functionality of the endpoints

## Tech Stack 
Backend: Django, Django REST Framework
Storage: Cloudinary
Database: PostgreSQL 
Authentication: Token-based
Installation & Setup
Prerequisites
Python 3.8+
Django installed (pip install django djangorestframework)
Cloudinary account & API credentials

### This is my live video for task 4
https://drive.google.com/file/d/1bIk6PaMZ0f9vx1Zhl1YGMbbfHNV6vNVS/view?usp=sharing

# Task 5 - Evaluation API

## Overview  
The **Evaluation API** is responsible for managing candidate evaluations within the Vector Interview App.
It allows evaluators to review, score, and provide feedback on candidate responses.

## Features  
1. Submit evaluations for candidate responses.
2.  Retrieve candidate responses for review.
3.  Store and manage evaluator scores and feedback.
4.  Ensure secure authentication for evaluators.
5.  Automated scoring and aggregation of results.
6.  Tested API – Used Curl command to verify endpoint functionality.  

## Technologies Used  
- **Backend**: Python(Django) 
- **Database**: PostgreSQL  
- **Authentication**: OAuth 2.0  
- **Security**: Data encryption, GDPR compliance  

## API Endpoints  

| Method | Endpoint                         | Description                          | Authentication |
|--------|----------------------------------|--------------------------------------|---------------|
| POST   | `/api/evaluations`              | Submit a new evaluation             | Required   |
| GET    | `/api/evaluations/candidate/:id` | Get all evaluations for a candidate | Required   |

## Authentication  
- Uses **authentication token** for secure access.  
- Evaluators must be authenticated before submitting or retrieving evaluations.  

## Testing  
Used **curl command** to test API functionality, ensuring proper request handling, authentication, and data validation.

## License  
This project is licensed under the MIT License.


