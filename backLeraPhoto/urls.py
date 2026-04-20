from django.urls import path
from .views import BookingListCreateView, CurrentUserView, LoginView, BookingCategoryListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from backLeraPhoto.views import RegisterView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('bookings/', BookingListCreateView.as_view()),
    path('categories/', BookingCategoryListView.as_view(), name='booking-categories'),
    path('user/', CurrentUserView.as_view(), name='current_user'),
]