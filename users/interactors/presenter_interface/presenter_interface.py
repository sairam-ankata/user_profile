import abc
from typing import List, Optional

from users.interactors.dtos import UserDetailsDTO
from users.interactors.oauth_user_auth_tokens_service_interactor import UserAuthTokensDTO
from users.interactors.storage_interface.dtos import UserResumeDetailsDTO


class PresenterInterface:

    @abc.abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abc.abstractmethod
    def prepare_user_auth_token_response(self, user_auth_token_dto: UserAuthTokensDTO):
        pass

    @abc.abstractmethod
    def raise_user_name_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def raise_email_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def prepare_user_details(
            self, user_details_dto: UserDetailsDTO,
            user_resume_details: Optional[List[UserResumeDetailsDTO]]):
        pass

    @abc.abstractmethod
    def raise_user_profile_already_deleted_exception(self):
        pass

    @abc.abstractmethod
    def success_response(self):
        pass
