from fastapi import FastAPI

from feat.auth.routes import LoginRouter
from feat.todo.routes import TodoRouter

app = FastAPI()

# Include routers for each feature
app.include_router(LoginRouter(), prefix="/api")
app.include_router(TodoRouter(), prefix="/api")