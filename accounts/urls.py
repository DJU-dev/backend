from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('allauth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('profile/<int:pk>/', views.ProfileView.as_view()),
    path('my/profile/', views.MyProfileView.as_view()),
]