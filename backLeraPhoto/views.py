from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import permissions
from .models import Booking, BookingCategory, BookingChat
from .serializers import BookingSerializer, BookingCategorySerializer, BookingChatSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView

class BookingCategoryListView(generics.ListAPIView):
    queryset = BookingCategory.objects.all()
    serializer_class = BookingCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingChatListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        booking_id = self.kwargs['booking_id']
        booking = generics.get_object_or_404(Booking, id=booking_id)
        if booking.user != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("You do not have access to this booking")
        return BookingChat.objects.filter(booking=booking)

    def perform_create(self, serializer):
        booking = generics.get_object_or_404(Booking, id=self.kwargs['booking_id'])
        if booking.user != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("You cannot message in this booking")
        serializer.save(author=self.request.user, booking=booking)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            response = Response({'message': 'Logged out successfully'})
            response.delete_cookie('access_token')
            response.delete_cookie('refresh_token')
            
            return response
            
        except Exception as e:
            response = Response({'message': 'Logged out'})
            response.delete_cookie('access_token')
            response.delete_cookie('refresh_token')
            return response

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserDetailUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)

            response = Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            })

            response.set_cookie(
                'access_token',
                str(refresh.access_token),
                httponly=True,
                samesite='Lax',
                secure=False,
                path='/',
                max_age=30 * 60,
            )
            response.set_cookie(
                'refresh_token',
                str(refresh),
                httponly=True,
                samesite='Lax',
                secure=False,
                path='/',
                max_age=1 * 24 * 60 * 60,
            )

            return response
        else:
            return Response({'error': 'Invalid credentials'}, status=401)