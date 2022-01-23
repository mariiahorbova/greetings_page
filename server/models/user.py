from pydantic import BaseModel, Field
from fastapi import Form


class UserSchema(BaseModel):
    name: str
    surname: str

    @classmethod
    def as_form(cls, name: str = Form(...), surname: str = Form(...)):
        return cls(name=name, surname=surname)


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
