import uvicorn
from fastapi import FastAPI

from application.handler import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("application.app:app", host="0.0.0.0", reload=False, port=5000, log_level="info")
