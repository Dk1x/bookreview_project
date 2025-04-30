from django.urls import path
from .views import (
    RegisterView,ChangePasswordView,BookListCreateView,BookRetrieveUpdateDestroyView,ReviewListCreateView, ReviewRetrieveUpdateDestroyView, TokenObtainView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book_detail_update_delete'),

    path('books/<int:book_id>/reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review_update_delete'),
]