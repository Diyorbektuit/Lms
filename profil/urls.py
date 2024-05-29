from django.urls import path
from .views import profile, update_name
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile_update/', update_name, name='profile_update'),

]