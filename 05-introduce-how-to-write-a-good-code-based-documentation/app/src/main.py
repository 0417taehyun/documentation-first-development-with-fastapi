import uvicorn
from fastapi import FastAPI

from src.constant import APIVersion
from src.router import v1, v2


app = FastAPI(openapi_url=None)
app.mount(path=APIVersion.V1.value, app=v1.app, name="The first version of API")
app.mount(path=APIVersion.V2.value, app=v2.app, name="The second version of API")


if __name__ == "__main__":
    uvicorn.run(app="src.main:app", reload=True)
