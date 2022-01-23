from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from server.routes.user import router as UserRouter
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})