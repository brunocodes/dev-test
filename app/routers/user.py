from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, user_crud
from fastapi.encoders import jsonable_encoder
import logging


logger = logging.getLogger("devtest")

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate):

    logger.debug(f"POST /users/User request UserCreate: ", user.dict())

    new_user = await user_crud.create_user(user)

    logger.info(f"POST /users/User response UserOut: ", new_user.dict())

    return new_user


@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(user_id: int):

    logger.debug(f"GET /users/id request user_id: ", user_id)

    user = await user_crud.fetch_one_user(user_id)

    if not user:
        logger.info(f"GET /users/id, User with id: {user_id} does not exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {user_id} does not exist")

    logger.info(f"GET /users/id response UserOut: ", user)

    return user
    

@router.put('/{user_id}', response_model=schemas.UserOut)
async def update_user(user_id: str, user: schemas.UserUpdate):
    logger.debug(f"User request user_id: ", user_id)
    user_res = await user_crud.update_user(user)
    if not user_res:
        logger.info(f"User with id: {user_id} does not exist")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {user_id} does not exist")

    return user_res

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):

    logger.debug(f"DELETE /users/User/id request user_id: ", user_id)

    delete_res = await user_crud.remove_user(user_id)

    if delete_res == 1:
        logger.info(f"DELETE /users/User/{user_id} response 204, OK")
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    logger.debug(f"DELETE /users/User/id response, User with id: {user_id} does not exist")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with id: {user_id} does not exist")