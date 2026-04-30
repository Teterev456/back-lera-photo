from django.urls import path
from .views import BookingListCreateView, CurrentUserView, LoginView, BookingCategoryListView, BookingChatListCreateView, UserDetailUpdateView, ContactMessageCreateView, AllBookingsListView
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
    path('user/update/', UserDetailUpdateView.as_view(), name='user-detail'),
    path('bookings/<int:booking_id>/messages/', BookingChatListCreateView.as_view()),
    path('contact/', ContactMessageCreateView.as_view(), name='contact'),

    path('admin/bookings/', AllBookingsListView.as_view(), name='admin-bookings')
]
