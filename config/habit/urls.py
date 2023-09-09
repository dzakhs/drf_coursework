from config.habit.apps import HabitConfig
from django.urls import path

from config.habit.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitConfig.name





urlpatterns = [
    path('habit/', HabitListAPIView.as_view(), name='habit'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/',HabitDestroyAPIView.as_view(), name='habit-delete'),


]