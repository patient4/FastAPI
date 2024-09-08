from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from CONSTANTS import COLLECTION
from config.firebase import Firebase
from modal.todo import Todo
from schema.todo import todoEntity
router = APIRouter()

templates = Jinja2Templates(directory="templates")

firebase_service = Firebase()

 

@router.get("/todos", response_class=HTMLResponse)
async def read_todos(request: Request):
    todos = firebase_service.read_docs(COLLECTION)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@router.get('/db')
async def db_init(request: Request):
    # return {"collections" : docs}
    pass


@router.post("/todos/createTodo")
async def create_todo(request: Todo):
    payload = request.model_dump()
    docs = firebase_service.create_doc(COLLECTION, payload=payload)
    return RedirectResponse(url='/todos', status_code=303)
