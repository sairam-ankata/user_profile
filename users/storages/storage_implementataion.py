from typing import Optional, List

from users import models
from users.exceptions import exceptions
from users.interactors.dtos import UserDetailsDTO
from users.interactors.storage_interface.dtos import UserResumeDetailsDTO
from users.interactors.storage_interface.storage_interface import StorageInterface


class StorageImplementation(StorageInterface):

    def validate_user_name_and_get_user_id(self, user_name: str) -> Optional[int]:
        try:
            user_obj = models.User.objects.get(username=user_name)
        except models.User.DoesNotExist:
            raise exceptions.InvalidUserNameException()
        if user_obj.is_deleted is True:
            raise exceptions.UserProfileAlreadyDeletedException()

        return user_obj.id

    def validate_password(self, user_name: str, password: str):
        user_obj = models.User.objects.get(username=user_name)
        if not user_obj.check_password(password):
            raise exceptions.InvalidPasswordException()

    def create_user_account(self, user_name: str, password: str):
        try:
            models.User.objects.get(username=user_name)
        except models.User.DoesNotExist:
            user_obj = models.User(username=user_name)
            user_obj.set_password(password)
            user_obj.save()
            return user_obj.id
        raise exceptions.UserNameAlreadyExistsException()

    def get_user_details(self, user_id) -> UserDetailsDTO:
        user_obj = models.User.objects.get(id=user_id)
        if user_obj.is_deleted is True:
            raise exceptions.UserProfileAlreadyDeletedException()
        return UserDetailsDTO(
            user_id=user_obj.id,
            user_name=user_obj.username,
            email=user_obj.email,
            first_name=user_obj.first_name,
            last_name=user_obj.last_name
        )

    def validate_user_name(self, user_name: str):
        if models.User.objects.filter(username=user_name).exists():
            raise exceptions.UserNameAlreadyExistsException()

    def validate_email(self, email: str):
        if models.User.objects.filter(email=email).exists():
            raise exceptions.EmailAlreadyExistsException()

    def update_user_details(self, user_details: UserDetailsDTO):
        print("********"*100, user_details)
        models.User.objects.filter(id=user_details.user_id).update(
            username=user_details.user_name,
            email=user_details.email,
            first_name=user_details.first_name,
            last_name=user_details.last_name)

    def get_user_resume_details(self, user_id: int) -> List[UserResumeDetailsDTO]:
        user_resume_objs = models.UserResume.objects.filter(user_id=user_id)
        return [
            UserResumeDetailsDTO(
                user_id=user_id,
                resume_url=each.url,
                adding_date=each.date_of_adding
            )
            for each in user_resume_objs
        ]

    def soft_delete_user_profile(self, user_id: int):
        models.User.objects.filter(id=user_id).update(is_deleted=True)

    def attach_resume_to_profile(self, user_id: int, resume_url: str):
        models.UserResume.objects.create(user_id=user_id, url=resume_url)
