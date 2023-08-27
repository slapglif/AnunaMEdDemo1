"""
@author: Kuro
"""
from fastapi import APIRouter, Depends, Request

from app.shared.middleware.auth import JWTBearer


router = APIRouter(
    prefix="/api/user", dependencies=[], tags=["infer"]
)


@router.post("/start_conversation", re)
def

