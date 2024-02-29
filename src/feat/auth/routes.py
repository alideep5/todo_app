from fastapi import APIRouter

class LoginRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.add_api_route("/login", self.perform_login, methods=["GET"])

    async def perform_login(self):
        return {"message": "This is Login API"}