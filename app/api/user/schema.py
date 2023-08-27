"""
@author: Kuro
"""
from datetime import datetime
from typing import List, Optional, Union
from uuid import UUID

from fastapi_camelcase import CamelModel
from pydantic import BaseModel, Field

from app.api.auth.schema import TokenDetail, TokenResponse
from app.shared.redis.redis_services import JsonMixin
from app.shared.schemas.ResponseSchemas import BaseResponse, PagedBaseResponse
from app.shared.schemas.orm_schema import ORMCamelModel
from app.shared.schemas.page_schema import GetPages, PagedResponse


class UserCredit(JsonMixin):
    balance: Optional[float]
    updated_at: Optional[datetime]

class User(JsonMixin):
    id: Optional[int]
    phone: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    balance: Optional[UserCredit]
    username: Optional[str]
    created_at: Optional[datetime]
    active: Optional[bool]

class LoadUserResponse(BaseResponse):
    """
    `LoadUserResponse` is a class that is used to validate the data that is being passed to the `/user` route.
    """

    response: Optional[User]

class AgentUserCreateResponse(BaseResponse):
    """
    `UserCreateResponse` is a class that is used to validate the data that is being passed to the `/user` route.
    """

    success: bool = Field(default=False)
    response: Optional[Union[User, TokenDetail]]

class AdminUserCreateResponse(TokenResponse):
    """
    `AdminUserCreateResponse` is a class that is used to validate the data that is being passed to the `/user` route.
    """

    response: Optional[Union[User, TokenDetail]]

class AdminUserCreate(CamelModel):
    """
    `UserCreate` is a class that is used to validate the data that is being passed to the `/user` route.
    """

    email: str
    password: str
    username: str

class AgentUserCreate(CamelModel):
    """
    `UserCreate` is a class that is used to validate the data that is being passed to the `/user` route.
    """

    phone: str
    password: str
    username: str
    quota: Optional[int]

class UserLogin(CamelModel):
    """
    A class that is used to validate the data that is being passed to the `/login` route.
    """

    phone: str
    password: str

class AdminLogin(CamelModel):
    """
    This is a class that is used to validate the data that is being passed to the `/admin/login` route.

    """

    phone: str
    password: str


    class Config:
        schema_extra = { "example": { "email": "test@test.com", "password": "1234567" } }

class AgentLogin(CamelModel):
    """
    This is a class that is used to validate the data that is being passed to the route.

    """

    phone: str
    password: str


    class Config:
        schema_extra = { "example": { "email": "test@test.com", "password": "1234567" } }

class UserResponse(BaseResponse):
    """
    `UserResponse` is a class that is used to validate the data that is being passed to the `/login` route.
    """

    error: Optional[str]
    response: Optional[AdminUserCreate]
    success: Optional[bool]

class GetUser(CamelModel):
    """
    `GetUser` is a class that is used to validate the data that is being passed to the `/user/{userId}` route.
    """

    id: int

class AdminBaseResponse(ORMCamelModel):
    """
    `UserBaseResponse` is a class that is used to validate the data that is being passed to the `/user/{userId}` route.

    """

    success: bool
    error: Optional[str]
    response: Optional[UUID]
    username: Optional[str]
    username: Optional[str]
    created_at: Optional[datetime]
    response: Optional[UUID]

class AdminUpdateName(CamelModel):
    """
    This is a class that is used to validate the data that is being passed to the `/user/{userId}/update/name` route.

    """

    username: str

class AdminUpdateNameResponse(BaseResponse):
    """
    A class that is used to validate the data that is being passed to the `/user/{userId}/update/name` route.

    """

    success: bool
    error: Optional[str]

class CLaimAuthPayload(ORMCamelModel):
    """
    This class is used to claim a user's account
    """

    id: int
    phone: str

class IGetUserList(CamelModel):
    filter: Optional[GetUser]

class GetAllUsers(GetPages):
    context: Optional[IGetUserList]

class GetUserListItems(PagedResponse):
    items: List[User]

class GetUserListResponse(PagedBaseResponse):
    response: Optional[GetUserListItems]

class GeneratePassword(BaseModel):
    id: int = Field(..., alias="userId")

class NewPassword(CamelModel):
    password: Optional[str]

class GeneratePasswordResponse(BaseResponse):
    response: Optional[NewPassword]

class RemoveUser(CamelModel):
    """
    It's a model that is used to remove a user from the database.
    """

    id: int
    email: Optional[str]

class UpdateUserResponse(BaseResponse):
    """
    It's a model that represents a user that is being updated.
    """

    response: Optional[User]

class RemovedUser(BaseModel):
    """
    It's a model that represents a user that is being updated.
    """

    id: int
    email: Optional[str]

class RemoveUserResponse(BaseResponse):
    """
    It's a model that represents a user that is being updated.
    """

    response: Optional[RemovedUser]

class AgentCreateUserResponse(BaseResponse):
    """
    `AgentCreateResponse` is a model that is used to return a response from the `/user` route.
    """

    response: Optional[User]

class UpdateUser(CamelModel):
    """
    It's a model that represents a user that is being updated.
    """

    id: int
    phone: Optional[str]
    username: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    active: Optional[bool]
