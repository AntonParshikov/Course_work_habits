from datetime import time

from rest_framework import serializers


class HabitValidator:

    def __call__(self, value):
        if value.get('related_habit') and value.get('reward'):
            raise serializers.ValidationError('Связанную привычку и вознаграждение нельзя указывать вместе')
        if time(0, 2) > value.get('execution_time'):
            raise serializers.ValidationError('Время выполнения не должно превышать 2 минуты')
        if value.get('related_habit') and not value.get('related_habit').is_pleasant:
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки')
        if value.get('related_habit') and value.get('reward'):
            raise serializers.ValidationError(
                'У приятной привычки не может быть вознаграждения или связанной привычки.')
        if value.get('frequency') > 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')


