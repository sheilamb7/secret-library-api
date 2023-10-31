from fastapi import FastAPI
from routes.challenge import router as challenge_router
from routes.prompt import router as prompt_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://secret-library-react.onrender.com",
    "https://secret-library-react.onrender.com/challenges/*"
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


