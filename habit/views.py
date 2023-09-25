from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from habit.models import Habit
from habit.serializers import HabitSerializer


class HabitListView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitCreateView(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDeleteView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
