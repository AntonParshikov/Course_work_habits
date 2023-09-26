from django.urls import path
from habit.apps import HabitConfig
from habit.views import HabitListView, HabitRetrieveView, HabitCreateView, HabitUpdateView, HabitDeleteView

app_name = HabitConfig.name

urlpatterns = [
    path('habit/', HabitListView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', HabitRetrieveView.as_view(), name='habit_list'),
    path('habit/create/', HabitCreateView.as_view(), name='habit_list'),
    path('habit/update/<int:pk>/', HabitUpdateView.as_view(), name='habit_list'),
    path('habit/delete/<int:pk>/', HabitDeleteView.as_view(), name='habit_list'),
]
