from fastapi import APIRouter
from models.prompt import Prompt

router = APIRouter()

prompts = [
    {"prompts_id" : 1, "prompts_challenge_id": 1, "prompts_content": "Read a book with a red cover", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 2, "prompts_challenge_id": 1, "prompts_content": "Read a book with a orange cover", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 3, "prompts_challenge_id": 1, "prompts_content": "Read a book with a yellow cover", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 4, "prompts_challenge_id": 1, "prompts_content": "Read a book with a green cover", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 5, "prompts_challenge_id": 1, "prompts_content": "Read a book with a blue cover", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 6, "prompts_challenge_id": 1, "prompts_content": "Read a book with a purple cover", "prompts_completed" : 1, "prompts_completed_book": "Hellfriend"},
    {"prompts_id" : 7, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter A", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 8, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter B", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 9, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter C", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 10, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter D", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 11, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter E", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 12, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter F", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 13, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter G", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 14, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter H", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 15, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter I", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 16, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter J", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 17, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter K", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 18, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter L", "prompts_completed" : 1, "prompts_completed_book": "Lord of the Rings"},
    {"prompts_id" : 19, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter M", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 20, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter N", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 21, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter O", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 22, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter P", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 23, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter Q", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 24, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter R", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 25, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter S", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 26, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter T", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 27, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter U", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 28, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter V", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 29, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter W", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 30, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter X", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 31, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter Y", "prompts_completed" : 0, "prompts_completed_book": ""},
    {"prompts_id" : 32, "prompts_challenge_id": 2, "prompts_content": "Read a book that starts with letter Z", "prompts_completed" : 0, "prompts_completed_book": ""}
]

@router.get("/prompts")
def get_prompts():
    return prompts

@router.get("/prompts/{prompts_id}")
def get_prompt(prompts_id: int):
    return list(filter(lambda item:item['prompts_id'] == prompts_id, prompts))

@router.get("/prompts_list/{prompts_challenge_id}")
def get_prompt(prompts_challenge_id: int):
    return list(filter(lambda item:item['prompts_challenge_id'] == prompts_challenge_id, prompts))

@router.get("/prompts/")
def get_prompt_by_name(prompts_content: str):
    return list(filter(lambda item:item['prompts_content'] == prompts_content, prompts))

@router.post("/prompts")
def create_prompt(prompt: Prompt):
    prompts.append(prompt)
    return prompts

@router.put("/prompts/{prompts_id}")
def update_prompt(prompts_id: int, prompt: Prompt):
    for p in prompts:
        if p["prompts_id"] == prompts_id:
            p["prompts_completed_book"] = prompt.prompts_completed_book
            return {"message": "Book updated succesffully"}
        return {"error" : "can't update book"}

    # for index, item in enumerate(prompts):
    #     if item['prompts_id'] == prompts_id:
    #         prompt[index]['prompts_challenge_id'] = prompt.prompts_challenge_id
    #         prompt[index]['prompts_name'] = prompt.prompts_content
    #         prompt[index]['prompts_completed'] = prompt.prompts_completed
    #         prompt[index]['prompts_completed_book'] = prompt.prompts_completed_book
    # return prompts

@router.delete("prompts/{prompts_id}")
def delete_prompt(prompts_id: int):
    for item in prompts:
        if item['prompts_id'] == prompts_id:
            prompts.remove(item)
    return prompts