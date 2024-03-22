import uvicorn
from fastapi import FastAPI

from src.constant import APIBoundary
from src.router import private, public


app = FastAPI(openapi_url=None)
app.mount(path=APIBoundary.PRIVATE.value, app=private.app, name="A private API")
app.mount(path=APIBoundary.PUBLIC.value, app=public.app, name="A public API")


if __name__ == "__main__":
    uvicorn.run(app="src.main:app", reload=True)
