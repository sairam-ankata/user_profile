from users.exceptions import exceptions
from users.interactors.storage_interface.storage_interface import StorageInterface
from users.interactors.presenter_interface.presenter_interface import PresenterInterface


class SoftDeleteUserProfileInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def soft_delete_user_profile_wrapper(self, user_id: int, presenter: PresenterInterface):
        try:
            self.soft_delete_user_profile(user_id=user_id)
        except exceptions.UserProfileAlreadyDeletedException:
            return presenter.raise_user_profile_already_deleted_exception()

        return presenter.success_response()

    def soft_delete_user_profile(self, user_id: int):
        self.storage.get_user_details(user_id=user_id)
        self.storage.soft_delete_user_profile(user_id=user_id)
