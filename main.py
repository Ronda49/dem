from fastapi import FastAPI, HTTPException

app = FastAPI()

# Fake in-memory database
fake_db = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

@app.get("/")
def root():
    return {"message": "Welcome to FakeDB API"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id in fake_db:
        return fake_db[user_id]
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/{user_id}")
def add_user(user_id: int, user: dict):
    if user_id in fake_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_db[user_id] = user
    return {"message": "User added successfully", "user": user}
