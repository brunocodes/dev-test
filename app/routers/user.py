from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, user_crud
 

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate):

    new_user = user_crud.create_user(**user.dict())

    return new_user


@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int):
    user = user_crud.fetch_one_user(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user


@router.put('/{id}', response_model=schemas.UserOut)
def update_user(user: schemas.UserUpdate):
    user = user_crud.update_user(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user
