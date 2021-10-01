import abc


class OAuthStorageInterface:
    @abc.abstractmethod
    def get_or_create_default_application(self, user_id):
        pass

    @abc.abstractmethod
    def create_access_token(self, user_id, application_id, scopes,
                            expiry_in_seconds):
        pass

    @abc.abstractmethod
    def create_refresh_token(self, user_id, application_id, access_token_id):
        pass
