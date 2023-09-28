from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from habit.models import Habit
from habit.paginators import HabitPagination
from habit.serializers import HabitSerializer
from users.permissions import IsOwner, IsAdmin


class HabitListView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)


class HabitRetrieveView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)


class HabitCreateView(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitUpdateView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)


class HabitDeleteView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)


class HabitPublicListView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_publication=True)
    pagination_class = HabitPagination
