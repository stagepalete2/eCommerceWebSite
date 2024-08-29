from django.urls import path
from .views import profile, edit_profile, signin, signup

urlpatterns = [
    path('', profile, name='profile'),
    path('edit/', edit_profile, name='edit'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
]