from typing import Final

from fastapi import Request, HTTPException, status


_IP_ALLOW_LIST: Final[list[str]] = ["127.0.0.1"]


async def validate_client_ip_address(request: Request) -> bool:
    ip_address: str = request.client.host
    if ip_address not in _IP_ALLOW_LIST:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden request.")

    return True
