import dataclasses
import datetime

from users.interactors.storage_interface.oauth_storage_interface import OAuthStorageInterface


@dataclasses.dataclass
class UserAuthTokensDTO:
    user_id: str
    access_token: str
    refresh_token: str
    expires_in: datetime.datetime


class OAuthUserAuthTokensServiceInteractor:
    def __init__(self, oauth_storage: OAuthStorageInterface):
        self.oauth_storage = oauth_storage

    def create_user_auth_tokens(self, user_id: str):
        from django.conf import settings
        application, _ = self.oauth_storage.get_or_create_default_application(
            user_id=user_id
        )
        access_token_obj = self.oauth_storage.create_access_token(
            user_id=user_id,
            application_id=application.application_id,
            scopes=settings.DEFAULT_OAUTH_SCOPES,
            expiry_in_seconds=settings.DEFAULT_ACCESS_TOKEN_EXPIRY_IN_SECONDS
        )

        refresh_token_obj = self.oauth_storage.create_refresh_token(
            user_id=user_id,
            application_id=application.application_id,
            access_token_id=access_token_obj.access_token_id
        )

        return UserAuthTokensDTO(
            user_id=user_id,
            access_token=access_token_obj.token,
            refresh_token=refresh_token_obj.token,
            expires_in=access_token_obj.expires
        )
