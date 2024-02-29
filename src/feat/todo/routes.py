from fastapi import APIRouter

class TodoRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.add_api_route("/todos", self.get_todos, methods=["GET"])

    async def get_todos(self):
        return {"message": "This is TODO'S API"}