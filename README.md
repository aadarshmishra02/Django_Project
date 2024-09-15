# Django_Project

This is a Django-based project with a REST API for managing clients and projects. The project is built using Django REST Framework (DRF) to handle CRUD operations for clients and their respective projects. It supports listing, adding, and managing clients and their related projects.

![Screenshot (163)](https://github.com/user-attachments/assets/29a1b59f-d764-4718-b246-bf905541f1bb)
![Screenshot (161)](https://github.com/user-attachments/assets/ce2ab645-9281-4eae-a380-0d630feb07a8)
![Screenshot (162)](https://github.com/user-attachments/assets/3d864e18-89d3-4f45-8bc6-7d704c071148)
![Screenshot (160)](https://github.com/user-attachments/assets/0436cb8b-8c5c-49e6-9553-b614358e2044)

## Features
- **Clients API**: Manage clients with the ability to list, retrieve, update, and delete.
- **Projects API**: Manage projects associated with specific clients.
- **User Project View**: Lists projects associated with the logged-in user.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)

## Installation

To get the project up and running locally, follow these steps:

### Prerequisites

- Python 3.x
- Django 4.x
- Django REST Framework
- Virtual Environment (`virtualenv`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nimap_project.git
   cd nimap_project
2. Set up a virtual environment:
   ```bash
   python -m venv Env
   source Env/bin/activate   # For Linux/Mac
   Env\Scripts\activate      # For Windows
3. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
4. Run the development server:
   ```bash
   python manage.py runserver
5. Access the API at:
   ```bash
   http://127.0.0.1:8000/

## Usage
Adding Clients and Projects
You can manually add clients and projects either by using the Django shell or through the API endpoints. For example:

1. Django Shell:
   ```bash
   python manage.py shell

2. Inside the shell, create a client:
   ```bash
   from DetailApp.models import Client
   Client.objects.create(name='Client 1', description='Example description')
   
3. API Usage: Use Postman or any API client to interact with the API endpoints to add, update, and retrieve clients and projects.

## API Endpoints

  | Endpoint                                        | Method | Description                                  |
  |-------------------------------------------------|--------|----------------------------------------------|
  | `/clients/`                                     | GET    | List all clients                             |
  | `/clients/{id}/`                                | GET    | Retrieve a specific client                   |
  | `/clients/`                                     | POST   | Create a new client                          |
  | `/clients/{id}/`                                | PUT    | Update a specific client                     |
  | `/clients/{id}/`                                | DELETE | Delete a specific client                     |
  | `/clients/{client_id}/projects/`                | GET    | List all projects under a specific client    |
  | `/clients/{client_id}/projects/{project_id}/`   | GET    | Retrieve a specific project                  |
  | `/projects/`                                    | GET    | List all projects assigned to the user       |

## Technologies Used
 - **Django**: Web framework used for the backend.
 - **Django REST Framework**: Used for building the REST API.
 - **MySQL**: Default database for development.
 - **Python 3.x**: Backend programming language.

