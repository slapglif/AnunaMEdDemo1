"""
@author: Kuro
"""
from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID

from fastapi_camelcase import CamelModel
from pydantic import BaseModel, Field

from app.api.agent.schema import AgentQuota, AgentUser
from app.api.credit.schema import UserCredit
from app.shared.schemas.ResponseSchemas import BaseResponse, PagedBaseResponse
from app.shared.schemas.orm_schema import ORMCamelModel
from app.shared.schemas.page_schema import (Filter, GetOptionalContextPages, PagedResponse)


class UpdateUser(CamelModel):
    """
    It's a model that represents a user that is being updated.
    """

    id: int
    password: Optional[str]
    username: Optional[str]

class RemoveUser(CamelModel):
    """
    It's a model that is used to remove a user from the database.
    """

    id: int

class GetAgent(CamelModel):
    # It's a user.
    id: UUID

class BaseUser(ORMCamelModel):
    """
    # `BaseUser` is a base class for the `User` class.
    It is used to represent the base fields that are common
    to all users.  This is used to reduce the amount of code
    that needs to be written in the `User` class.
    """

    id: int
    email: Optional[str]
    password: Optional[str]
    balance: Optional[UserCredit]

class Admin(ORMCamelModel):
    id: UUID
    email: Optional[str]
    username: Optional[str]

class BaseUserResponse(ORMCamelModel):
    """
    It's a model that is used to return a list of users.
    """

    id: int
    phone: Optional[str]
    username: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    quota: Optional[AgentQuota] = Field(default=AgentQuota(balance=0))
    balance: Optional[UserCredit]
    active: Optional[bool]
    createdByAdmin: Optional[AgentUser]
    createdByAgent: Optional[Admin]

class AdminPagedResponse(PagedResponse):
    """
    The AdminPagedResponse class is a PagedResponse class that is
    used to return a list of users
    """

    items: List[AgentUser]

class ListAdminUserResponse(PagedBaseResponse):
    """
    The ListUserResponse class is a PagedResponse class that is
    used to return a list of users
    """

    response: Optional[AdminPagedResponse]

class ListUserResponse(PagedResponse):
    """
    The ListUserResponse class is a PagedResponse class that is
    used to return a list of users
    """

    items: List[BaseUserResponse]

class GetUserlistQueryOptions(CamelModel):
    """
    GetUserlistQueryOptions is a model that is used to get a list of users.
    """

    active: Optional[bool] = Field(Default=True, description="Filter by active status")

class OptionalContextPagesFilter(Filter):
    """
    OptionalContextPagesFilter is a model that is used to get a list of users.
    that is used in the `/list` endpoint.
    """

    filter: Optional[GetUserlistQueryOptions]

class GetUserList(GetOptionalContextPages):
    """
    OptionalContextPages is a model that is used to get a list of users.
    that is used in the `/list` endpoint.
    """

    context: Optional[OptionalContextPagesFilter]

class BatchUsers(CamelModel):
    """
    BatchUsers is a model that is used to update multiple users at once.
    It is used in the `/batch` endpoint.
    """

    __root__: List[UpdateUser]

class AdminRoleCreate(BaseModel):
    """
    It's a model that represents the data required to create an Admin Role.
    """

    username: str
    parameters: Optional[Dict]

class AdminSetRole(BaseModel):
    """
    It's a model that represents the data required to create an Admin Role.
    """

    role_id: UUID
    ownerId: int
    parameters: Optional[Dict]

class SetUserRoleResponse(BaseResponse):
    """
    SetUserRoleResponse is a model that is used to return a
    response from setting a user's role.
    """

    success: bool
    error: Optional[str]

class SetPermsResponse(BaseResponse):
    """
    SetPermsResponse is a model that is used to return a
    response from setting a user's permissions.
    """

    success: bool
    error: Optional[str]

class SearchUser(CamelModel):
    """
    `SearchUser` is a model that is used to search for users.
    It is used in the `/search` endpoint.
    """

    phone: Optional[str]
    username: Optional[str]
    firstName: Optional[str]
    type: str


    class Config:
        schema_extra = {
            "example": {
                "pick one: email | username | firstName": "John123@gmail.com | John123 | John",
                "type": "agent | admin | user",
            }
        }

class SearchResults(BaseResponse):
    """
    `SearchResults` is a model that is used to return a list of users
    that match a search query.  It is used in the `/search` endpoint.

    """

    response: Optional[List[BaseUserResponse]]

class AgentCreateResponse(BaseResponse):
    # This is a model that is used to return a response from the database.  It is used in the `/batch` endpoint.
    success: bool
    error: Optional[str]
    response: Optional[AgentUser]

class AgentUpdate(CamelModel):
    agentId: UUID
    quota: Optional[int]
    active: Optional[bool]

class AgentUpdateResponse(BaseResponse):
    # This is a model that is used to return a response from the database.  It is used in the `/batch` endpoint.
    success: bool
    error: Optional[str]
    response: Optional[AgentUser]

class AdminUserUpdateName(CamelModel):
    username: str

# It's a model that is used to return a response from updating a user's name.  It is used in the `/admin` endpoint.


class AdminUserUpdateNameResponse(BaseResponse):
    success: bool
    error: Optional[str]

class AdminSetPassword(CamelModel):
    id: UUID
    password: str

class AdminSetPasswordResponse(BaseResponse):
    success: bool
    error: Optional[str]
