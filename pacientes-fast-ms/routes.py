from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import ListModel, ListUpdateModel

router = APIRouter()

@router.post("/", response_description='create a todo list', status_code=status.HTTP_201_CREATED,response_model=ListModel)
def create_list(request: Request, list: ListModel = Body(...)):
    list = jsonable_encoder(list)
    new_list_item = request.app.database["lists"].insert_one(list)
    created_list_item = request.app.database["lists"].find_one({
        "_id": new_list_item.inserted_id
    })

    return created_list_item
