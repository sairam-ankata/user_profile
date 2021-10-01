import datetime
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class UserDetailsDTO:
    user_id: int
    user_name: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

