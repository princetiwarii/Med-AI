from fastapi import FastAPI
from routers.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "Medical Chatbot Backend Running Successfully!"
    }