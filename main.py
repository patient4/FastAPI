from typing import Union
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes import todo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(todo.router)





