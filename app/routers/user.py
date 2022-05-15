from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, user_crud
from fastapi.encoders import jsonable_encoder

 

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate):
    new_user = await user_crud.create_user(user)
    return new_user


@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(user_id: int):
    user = await user_crud.fetch_one_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {user_id} does not exist")

    return user
    

@router.put('/{user_id}', response_model=schemas.UserOut)
async def update_user(user_id: str, user: schemas.UserUpdate):
    user_res = await user_crud.update_user(user)
    if not user_res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {user_id} does not exist")

    return user_res

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    delete_res = await user_crud.remove_user(user_id)
    if delete_res == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with id: {user_id} does not exist")