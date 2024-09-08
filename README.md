# FastAPI Todo App

A simple and efficient Todo application built with [FastAPI](https://fastapi.tiangolo.com/), an asynchronous web framework for Python. This application allows users to create, read, update, and delete todos, providing a basic example of how to use FastAPI for building RESTful APIs.

## Features

- **Create Todo**: Add a new todo item.
- **Read Todos**: List all todo items or get details of a specific todo item.

## Prerequisites

Ensure you have Python 3.7+ installed. You can check your Python version with:

```bash
python --version
```
## Installation

#### 1.Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-todo-app.git
cd fastapi-todo-app
```

#### 2.Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### 3.Install the dependencies:

```bash
pip install requirements.txt
```

#### 1.Run the application

```bash
uvicorn app.main:app --reload
```

### The application will be available at `http://127.0.0.1:8000`


## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Uvicorn](https://www.uvicorn.org/)



