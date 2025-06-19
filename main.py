from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

messages = []

@app.post("/send")
async def send_message(request: Request):
    data = await request.json()
    messages.append({
        "sender": data["sender"],
        "receiver": data["receiver"],
        "message": data["message"]
    })
    return {"status": "Message sent"}

@app.get("/messages")
def get_messages(receiver: str):
    return [msg for msg in messages if msg["receiver"] == receiver]
