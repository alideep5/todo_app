from fastapi import FastAPI

from feat.auth.routes import router as auth_router
from feat.todo.routes import router as todo_router

app = FastAPI()

# Include routers for each feature
app.include_router(auth_router, prefix="/api")
app.include_router(todo_router, prefix="/api")