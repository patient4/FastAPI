from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes import todo

# Initialize FastAPI application
app = FastAPI()

# Mount the static files directory to serve static assets like CSS, JavaScript, and images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the router from the 'todo' module for handling Todo-related routes
app.include_router(todo.router)
