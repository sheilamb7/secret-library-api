from pydantic import BaseModel, Field
from typing import Optional

class Challenge(BaseModel):
    challenges_id: int
    challenges_name: str 
    challenges_description: Optional[str]
    # challenges_description: str = Field(default = "New description". max-length= 300)
    # parametronumerico = Field(ge=0 #greater equal, le=0 #less equal, gt=0  #greater than)


    # https://www.youtube.com/watch?v=12NIB_RjxMo minut 37