import datetime
from dataclasses import dataclass


@dataclass
class UserResumeDetailsDTO:
    user_id: int
    resume_url: str
    adding_date: datetime
