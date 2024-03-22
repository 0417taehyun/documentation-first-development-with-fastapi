from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html

from src.constant import APIPath, APIBoundary
from src.middleware import validate_client_ip_address
from src.router.private import author


app = FastAPI(
    title="A private API",
    description="Describe how to seperate API through path for better security.",
    version="1.0.0",
    contact={"email": "0417taehyun@gmail.com"},
    openapi_url=None
)
app.include_router(router=author.router, prefix=APIPath.AUTHORS.value, tags=["Author"])


@app.get(path="/openapi.json", include_in_schema=None)
async def get_open_api_json(_: Annotated[bool, Depends(dependency=validate_client_ip_address)]):
    return get_openapi(title=app.title, version=app.version, routes=app.routes)


@app.get(path="/docs", include_in_schema=None)
async def get_swagger_ui(_: Annotated[bool, Depends(dependency=validate_client_ip_address)]):
    return get_swagger_ui_html(openapi_url=f"/{APIBoundary.PRIVATE.value}/openapi.json", title=app.title)
    