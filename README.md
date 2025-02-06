# crud_fastAPI
This repository provides an example of implementing CRUD (Create, Read, Update, Delete) operations using FastAPI and SQLAlchemy with a MySQL (or MariaDB) database. It showcases how to set up basic database interaction patterns in a FastAPI application while maintaining a clean, modular structure.
# FastAPI CRUD Application

This project is a basic CRUD (Create, Read, Update, Delete) application built with FastAPI and connected to a PostgreSQL database. It provides a simple way to manage user data and is designed for learning purposes.

## Features

- **Create**: Add new users to the database.
- **Read**: Retrieve user information.
- **Update**: Modify existing user details.
- **Delete**: Remove users from the database.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Installation

Follow these steps to set up the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/forgiveness-77/crud_fastAPI.git
   cd crud_fastAPI

2. **Set up a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate

3. **Install the Dependencies**

4. **Run the application:**
   ```bash
   uvicorn index:app --reload

