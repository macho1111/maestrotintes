from django.urls import path
from .views import UserProfileEditView

urlpatterns = [
    path('', UserProfileEditView.as_view(), name='profile_edit'),
]