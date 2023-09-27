from datetime import datetime
import requests
from celery import shared_task
from config.settings import TELEGRAM_TOKEN
from habit.models import Habit
from telebot import TeleBot
from users.models import User


@shared_task
def send_habit_message(pk):
    habit = Habit.objects.get(pk=pk)
    bot = TeleBot(TELEGRAM_TOKEN)
    message = f'Нужно выполнить {habit.action} в {habit.time} в {habit.place}'
    print(message)
    bot.send_message(habit.owner.tg_chat_id, message)
