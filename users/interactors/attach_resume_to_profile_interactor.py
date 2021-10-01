from users.interactors.storage_interface.storage_interface import StorageInterface
from users.interactors.presenter_interface.presenter_interface import PresenterInterface


class AttachResumeToUserProfileInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def attach_resume_to_profile_wrapper(
            self, user_id: int, resume_url: str, presenter: PresenterInterface):
        self.attach_resume_to_profile(user_id=user_id, resume_url=resume_url)
        return presenter.success_response()

    def attach_resume_to_profile(self, user_id: int, resume_url: str):
        self.storage.attach_resume_to_profile(
            user_id=user_id, resume_url=resume_url)
