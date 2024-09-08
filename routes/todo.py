from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from CONSTANTS import COLLECTION
from config.firebase import Firebase
from modal.todo import Todo
from schema.todo import todoEntity

router = APIRouter()

# Initialize Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Initialize Firebase service
firebase_service = Firebase()

@router.get("/todos", response_class=HTMLResponse)
async def read_todos(request: Request):
    """
    Fetches and displays all todos from the Firebase collection.

    Args:
        request (Request): The request object, which includes headers and other information.

    Returns:
        HTMLResponse: Renders the "index.html" template with the list of todos.
    """
    # Fetch todos from the Firebase collection
    todos = firebase_service.read_docs(COLLECTION)
    # Render and return the template with the todos data
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@router.get('/db')
async def db_init(request: Request):
    """
    Initializes the database. This is a placeholder endpoint.

    Args:
        request (Request): The request object, which includes headers and other information.

    Returns:
        dict: Placeholder response. Modify this as needed.
    """
    # Placeholder for database initialization
    # Potentially return a status or information about the database
    pass

@router.post("/todos/createTodo")
async def create_todo(request: Todo):
    """
    Creates a new todo item and redirects to the todos list.

    Args:
        request (Todo): The request body containing the new todo item details.

    Returns:
        RedirectResponse: Redirects to the "/todos" page with a status code of 303 (See Other).
    """
    # Convert the Todo object to a dictionary
    payload = request.model_dump()
    # Create a new document in the Firebase collection with the payload
    firebase_service.create_doc(COLLECTION, payload=payload)
    # Redirect to the todos list page
    return RedirectResponse(url='/todos', status_code=303)
