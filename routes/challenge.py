from fastapi import APIRouter
from models.challenge import Challenge

router = APIRouter()

challenges = [
    {"challenges_id": 1, "challenges_name": "Rainbow Challenge", "challenges_description": "Read a book for every color in the rainbow"},
	{"challenges_id": 2, "challenges_name" : "ABC Challenge", "challenges_description": "Read a book for every letter on the alphabet"}
]

@router.get("/challenges")
def get_challenges():
    return challenges

@router.get("/challenges/{challenges_id}")
def get_challenge(challenges_id: int):
    return list(filter(lambda item:item['challenges_id'] == challenges_id, challenges))

@router.get("/challenges/")
def get_challenge_by_name(challenges_name: str):
    return list(filter(lambda item:item['challenges_name'] == challenges_name, challenges))

@router.post("/challenges")
def create_challenge(challenge: Challenge):
    challenges.append(challenge)
    return challenges

@router.put("/challenges/{challenges_id}")
def update_challenge(challenges_id: int, challenge: Challenge):
    for index, item in enumerate(challenges):
        if item['challenges_id'] == challenges_id:
            challenge[index]['challenges_name'] = challenge.challenges_name
            challenge[index]['challenges_description'] = challenge.challenges_description
    return challenges

@router.delete("challenges/{challenges_id}")
def delete_challenge(challenges_id: int):
    for item in challenges:
        if item['challenges_id'] == challenges_id:
            challenges.remove(item)
    return challenges