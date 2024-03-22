from typing import Annotated, Any

from fastapi import APIRouter, status, Body


router = APIRouter()


@router.post(path="", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def handle_webhook_events(
    event: Annotated[
        dict[str, Any],
        Body(default=..., description="A payload of the webhook event.")
    ]
):
    """
    Description \n
        1. Handle webhook events

    """
    pass
