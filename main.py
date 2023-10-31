from fastapi import FastAPI
from routes.challenge import router as challenge_router
from routes.prompt import router as prompt_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # "*"
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000/challenges",
    "http://127.0.0.1:8000/prompts/*",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def message():
    return "<h1>API for secret library</h1><div>Includes challenges API and prompts API"

app.include_router(challenge_router)
app.include_router(prompt_router)


