"""
@author: Kuro
"""
from fastapi import APIRouter, Depends, Request

from app import logging
from app.api.user import schema
from app.api.user.models import User
from app.api.user.schema import (
    LoadUserResponse,
)
from app.shared.middleware.auth import JWTBearer


router = APIRouter(
    prefix="/api/user", dependencies=[Depends(JWTBearer())], tags=["user"]
)

logger = logging.getLogger("user")
logger.addHandler(logging.StreamHandler())

@router.post("/get_user", response_model=LoadUserResponse)
async def post_user_data(context: schema.GetUser, request: Request):
    """
    The post_user_data function is used to create a new user in the database.
    It takes a context argument, which is an instance of schema.GetUser.

    :param request:
    :param context:schema.GetUser: Used to Pass the user data to the function.
    :return: A GetUserResponse object.
    """
    user = User.get(id=context.id)
    return LoadUserResponse(success=True, response=user)

@router.get("/get_user", response_model=LoadUserResponse)
async def get_user_data(request: Request):
    """f
    The get_user_data function returns the user data for a given user.

    :param request:Request: Used to Get the user object from the request.
    :return: A dictionary with the user's name, email and is_superuser attributes.
    """
    user = request.user
    return LoadUserResponse(success=True, response=user)
