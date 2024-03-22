import uvicorn
from fastapi import FastAPI

from src.router import router


app = FastAPI(
    title="Simple API",
    description="Describe the fundamental concept of DFD(Documentation-First Developmemt).",
    version="1.0.0",
    contact={"email": "0417taehyun@gmail.com"}
)

app.include_router(router=router)


if __name__ == "__main__":
    uvicorn.run(app="src.main:app", reload=True)
