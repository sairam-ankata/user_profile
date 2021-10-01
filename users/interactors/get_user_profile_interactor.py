from users.interactors.storage_interface.storage_interface import StorageInterface
from users.interactors.presenter_interface.presenter_interface import PresenterInterface


class GetUserProfileInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_details_wrapper(self, user_id: int, presenter: PresenterInterface):
        user_details_dto, user_resume_details = self.get_user_details(user_id=user_id)
        return presenter.prepare_user_details(
            user_details_dto=user_details_dto, user_resume_details=user_resume_details)

    def get_user_details(self, user_id: int):
        user_details_dto = self.storage.get_user_details(user_id)
        user_resume_details = self.storage.get_user_resume_details(user_id)
        user_resume_details = self._sort_resume_by_date_of_adding(user_resume_details)

        return user_details_dto, user_resume_details

    @staticmethod
    def _sort_resume_by_date_of_adding(user_resume_details):
        return sorted(user_resume_details, key=lambda x: x.adding_date, reverse=True)
