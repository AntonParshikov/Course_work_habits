from django.urls import path
from habit.apps import HabitConfig
from habit.views import HabitListView

app_name = HabitConfig.name

urlpatterns = [
    path('habit/', HabitListView.as_view(), name='habit_list'),

]
