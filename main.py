from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/message")
def read_message():
    pod_name = os.getenv("HOSTNAME", "unknown-pod")
    return {"message": "Hello from the GitOps Backend!", "pod": pod_name}
