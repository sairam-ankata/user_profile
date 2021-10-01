from users.exceptions import exceptions
from users.interactors.dtos import UserDetailsDTO
from users.interactors.storage_interface.storage_interface import StorageInterface
from users.interactors.presenter_interface.presenter_interface import PresenterInterface


class UpdateUserProfileInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_user_profile_wrapper(self, user_details: UserDetailsDTO, presenter: PresenterInterface):
        try:
            self.update_user_profile(user_details=user_details)
        except exceptions.UserNameAlreadyExistsException:
            return presenter.raise_user_name_already_exists_exception()
        except exceptions.EmailAlreadyExistsException:
            return presenter.raise_email_already_exists_exception()
        return presenter.success_response()

    def update_user_profile(self, user_details: UserDetailsDTO):
        existing_user_details = \
            self.storage.get_user_details(user_id=user_details.user_id)
        print("before: ", user_details, existing_user_details)
        user_details_to_update = self._get_user_details_to_update(
            user_details=user_details, existing_user_details=existing_user_details)
        print("after: ", user_details, user_details_to_update)
        self.storage.update_user_details(user_details=user_details_to_update)

    def _get_user_details_to_update(
            self, user_details: UserDetailsDTO, existing_user_details: UserDetailsDTO):

        if user_details.user_name is not None and user_details.user_name != existing_user_details.user_name:
            self.storage.validate_user_name(user_name=user_details.user_name)
            existing_user_details.user_name = user_details.user_name
        if user_details.email is not None and user_details.email != existing_user_details.email:
            self.storage.validate_email(email=user_details.email)
            existing_user_details.email = user_details.email
        if user_details.first_name is not None and user_details.first_name != existing_user_details.first_name:
            existing_user_details.first_name = user_details.first_name
        if user_details.last_name is not None and user_details.last_name != existing_user_details.last_name:
            existing_user_details.last_name = user_details.last_name

        return existing_user_details
