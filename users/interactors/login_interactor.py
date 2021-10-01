from users.exceptions import exceptions
from users.interactors.storage_interface.oauth_storage_interface import OAuthStorageInterface
from users.interactors.storage_interface.storage_interface import StorageInterface
from users.interactors.presenter_interface.presenter_interface import PresenterInterface


class LoginInteractor:
    def __init__(
            self, storage: StorageInterface, oauth_storage: OAuthStorageInterface):
        self.storage = storage
        self.oauth_storage = oauth_storage

    def login_page_wrapper(self, user_name: str, password: str, presenter: PresenterInterface):
        try:
            user_auth_token_dto = self.login_page(user_name=user_name, password=password)
        except exceptions.InvalidPasswordException:
            return presenter.raise_invalid_password_exception()
        except exceptions.UserProfileAlreadyDeletedException:
            return presenter.raise_user_profile_already_deleted_exception()
        except exceptions.UserNameAlreadyExistsException:
            return presenter.raise_user_name_already_exists_exception()

        return presenter.prepare_user_auth_token_response(
            user_auth_token_dto=user_auth_token_dto)

    def login_page(self, user_name: str, password: str):
        try:
            user_id = self.storage.validate_user_name_and_get_user_id(user_name=user_name)
        except exceptions.InvalidUserNameException:
            user_id = self._create_user_account(user_name=user_name, password=password)

        self.storage.validate_password(user_name=user_name, password=password)

        from users.interactors.oauth_user_auth_tokens_service_interactor import \
            OAuthUserAuthTokensServiceInteractor
        oauth_interactor = \
            OAuthUserAuthTokensServiceInteractor(oauth_storage=self.oauth_storage)
        user_auth_token_dto = \
            oauth_interactor.create_user_auth_tokens(user_id=user_id)
        return user_auth_token_dto

    def _create_user_account(self, user_name: str, password: str) -> str:
        user_id = self.storage.create_user_account(user_name=user_name, password=password)
        return user_id
