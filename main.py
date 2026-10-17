from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}
@app.get("/items")
def read_items():
    return{"items":"it works well!!"}\

@app.get("/users")
def read_users(user_id: int = 1):
    return {"users": "User ID: {}".format(user_id)}