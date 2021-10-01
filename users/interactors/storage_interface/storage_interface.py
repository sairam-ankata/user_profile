import abc
from typing import List, Optional

from users.interactors.dtos import UserDetailsDTO
from users.interactors.storage_interface.dtos import UserResumeDetailsDTO


class StorageInterface:
    @abc.abstractmethod
    def validate_user_name_and_get_user_id(self, user_name: str) -> Optional[int]:
        pass

    @abc.abstractmethod
    def validate_password(self, user_name: str, password: str):
        pass

    @abc.abstractmethod
    def create_user_account(self, user_name: str, password: str):
        pass

    @abc.abstractmethod
    def get_user_details(self, user_id) -> UserDetailsDTO:
        pass

    @abc.abstractmethod
    def validate_user_name(self, user_name: str):
        pass

    @abc.abstractmethod
    def validate_email(self, email: str):
        pass

    @abc.abstractmethod
    def update_user_details(self, user_details: UserDetailsDTO):
        pass

    @abc.abstractmethod
    def get_user_resume_details(self, user_id: int) -> List[UserResumeDetailsDTO]:
        pass

    @abc.abstractmethod
    def soft_delete_user_profile(self, user_id: int):
        pass

    def attach_resume_to_profile(self, user_id: int, resume_url: str):
        pass
