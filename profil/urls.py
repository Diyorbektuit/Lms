from django.urls import path
from .views import profile, update_name, update_password
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile_update/', update_name, name='profile_update'),
    path('update_password/', update_password, name='update_password'),

]