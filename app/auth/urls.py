from django.urls import path

from auth.api import views

urlpatterns = [
    path('token/', views.ObtainJSONWebTokenView.as_view()),
    path('token/refresh/', views.RefreshJSONWebTokenView.as_view()),
]