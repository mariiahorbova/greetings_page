from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from server.database import (
    add_user,
    retrieve_user,
    retrieve_users,
)
from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/", response_description="user data added into the database")
async def add_user_data(request: Request, user: UserSchema = Depends(UserSchema.as_form)):
    new_user = await add_user(user.dict())
    if new_user:
        return templates.TemplateResponse('user.html', {'request': request, 'name': new_user["name"],
                                                        'surname': new_user["surname"], "new_user": True})
    else:
        return templates.TemplateResponse('user.html', {'request': request, 'name': user.name,
                                                        'surname': user.surname, "new_user": False})


@router.get("/all", response_description="users retrieved")
async def get_users(request: Request):
    users = await retrieve_users()
    if users:
        return templates.TemplateResponse('users.html', {'request': request, 'users': users})
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", response_description="user data retrieved")
async def get_user_data(request: Request, id):
    user = await retrieve_user(id)
    if user:
        return templates.TemplateResponse('user.html', {'request': request, 'name': user["name"],
                                                        'surname': user["surname"]})
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")
