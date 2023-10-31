from pydantic import BaseModel, Field
from typing import Optional

class Prompt(BaseModel):
    prompts_id: int
    prompts_challenge_id: int
    prompts_content: str 
    prompts_completed: bool = Field(default=0)
    prompts_completed_book: str = Field(default="")
    # challenges_description: str = Field(default = "New description". max-length= 300)
    # parametronumerico = Field(ge=0 #greater equal, le=0 #less equal, gt=0  #greater than)


    # https://www.youtube.com/watch?v=12NIB_RjxMo minut 37