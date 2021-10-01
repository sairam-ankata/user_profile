import json
from typing import List, Optional

from django.http import HttpResponse

from users.interactors.dtos import UserDetailsDTO
from users.interactors.presenter_interface.presenter_interface import PresenterInterface
from users.interactors.oauth_user_auth_tokens_service_interactor import UserAuthTokensDTO
from users.interactors.storage_interface.dtos import UserResumeDetailsDTO
from users.constants import exception_messages


class PresenterImplementation(PresenterInterface):
    def raise_invalid_password_exception(self):
        data = {
            "res_status": exception_messages.INVALID_PASSWORD_EXCEPTION[0],
            "message": exception_messages.INVALID_PASSWORD_EXCEPTION[1]
        }
        data = json.dumps(data)
        return HttpResponse(data, content_type="application/json",
                            status=exception_messages.INVALID_PASSWORD_EXCEPTION[2])

    def prepare_user_auth_token_response(self, user_auth_token_dto: UserAuthTokensDTO):
        data = {
            "user_id": user_auth_token_dto.user_id,
            "access_token": user_auth_token_dto.access_token,
            "refresh_token": user_auth_token_dto.refresh_token,
            "expires_in": self._convert_datetime_to_str(user_auth_token_dto.expires_in)
        }
        data = json.dumps(data)
        return HttpResponse(data, content_type="application/json", status=200)

    def raise_user_name_already_exists_exception(self):
        data = {
            "res_status": exception_messages.USER_NAME_ALREADY_EXISTS_EXCEPTION[0],
            "message": exception_messages.USER_NAME_ALREADY_EXISTS_EXCEPTION[1]
        }
        data = json.dumps(data)
        return HttpResponse(data, content_type="application/json",
                            status=exception_messages.USER_NAME_ALREADY_EXISTS_EXCEPTION[2])

    def raise_email_already_exists_exception(self):
        data = {
            "res_status": exception_messages.EMAIL_ALREADY_EXISTS_EXCEPTION[0],
            "message": exception_messages.EMAIL_ALREADY_EXISTS_EXCEPTION[1]
        }
        data = json.dumps(data)
        return HttpResponse(data, content_type="application/json",
                            status=exception_messages.EMAIL_ALREADY_EXISTS_EXCEPTION[2])

    def prepare_user_details(
            self, user_details_dto: UserDetailsDTO,
            user_resume_details: Optional[List[UserResumeDetailsDTO]]):
        data = {
            "user_id": user_details_dto.user_id,
            "first_name": user_details_dto.first_name,
            "last_name": user_details_dto.last_name,
            "email": user_details_dto.email,
            "user_resumes": [
                {
                    "resume_url": each.resume_url,
                    "added_on": self._convert_datetime_to_str(each.adding_date)
                }
                for each in user_resume_details
            ]
        }
        data = json.dumps(data)
        return HttpResponse(data, content_type="application/json", status=200)

    @staticmethod
    def _convert_datetime_to_str(datetime_obj):
        date_time = datetime_obj.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time

    def raise_user_profile_already_deleted_exception(self):
        data = {
            "res_status": exception_messages.USER_PROFILE_DELETED_EXCEPTION[0],
            "message": exception_messages.USER_PROFILE_DELETED_EXCEPTION[1]
        }
        data = json.dumps(data)
        return HttpResponse(data, content_type="application/json",
                            status=exception_messages.USER_PROFILE_DELETED_EXCEPTION[2])

    def success_response(self):
        return HttpResponse("success response", status=200)
