from django.http import HttpResponse
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from users.interactors.dtos import UserDetailsDTO
from users.presenters.presenter_implementation import PresenterImplementation
from users.storages.storage_implementataion import StorageImplementation


@api_view(['POST'])
def user_login(request):
    from users.interactors.login_interactor import LoginInteractor
    from users.storages.oauth_storage_implementation import OAuthStorageImplementation
    interactor = LoginInteractor(
        storage=StorageImplementation(),
        oauth_storage=OAuthStorageImplementation())
    return interactor.login_page_wrapper(
        user_name=request.data.get("user_name"),
        password=request.data.get("password"),
        presenter=PresenterImplementation())


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, OAuth2Authentication])
@permission_classes([IsAuthenticated])
def user_details(request):
    if request.method == "GET":
        from users.interactors.get_user_profile_interactor import GetUserProfileInteractor
        interactor = GetUserProfileInteractor(storage=StorageImplementation())
        user = request.user
        return interactor.get_user_details_wrapper(
            user_id=user.id, presenter=PresenterImplementation())
    elif request.method == "POST":
        from users.interactors.update_user_profile_interactor import UpdateUserProfileInteractor
        interactor = UpdateUserProfileInteractor(storage=StorageImplementation())
        user = request.user
        request_data = request.data
        user_details_dto = UserDetailsDTO(
            user_id=user.id,
            user_name=request_data.get("user_name"),
            email=request_data.get("email"),
            first_name=request_data.get("first_name"),
            last_name=request_data.get("last_name"),
        )
        return interactor.update_user_profile_wrapper(
            user_details=user_details_dto,
            presenter=PresenterImplementation())
    elif request.method == "DELETE":
        from users.interactors.soft_delete_user_profile_interactor import SoftDeleteUserProfileInteractor
        interactor = SoftDeleteUserProfileInteractor(storage=StorageImplementation())
        user = request.user
        return interactor.soft_delete_user_profile_wrapper(
            user_id=user.id, presenter=PresenterImplementation())


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, OAuth2Authentication])
@permission_classes([IsAuthenticated])
def user_resume(request):
    from users.interactors.attach_resume_to_profile_interactor import AttachResumeToUserProfileInteractor
    interactor = AttachResumeToUserProfileInteractor(storage=StorageImplementation())
    user = request.user
    request_data = request.data
    return interactor.attach_resume_to_profile_wrapper(
        user_id=user.id, resume_url=request_data["resume_url"],
        presenter=PresenterImplementation())

