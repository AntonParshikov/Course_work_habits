from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habit.models import Habit
from users.models import UserRoles, User
from rest_framework_simplejwt.tokens import RefreshToken


class HabitTestCase(APITestCase):

    def setUp(self):
        """Заполнение первичных данных"""

        self.user = User.objects.create(
            email='test@test.ru',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.owner,
        )
        self.user.set_password('324214Kross!')
        self.user.save()

        token = RefreshToken.for_user(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.habit = Habit.objects.create(
            place='home',
            time="15:30:00",
            action="learn",
            is_pleasant=True,
            frequency=1,
            execution_time="00:02:00",
            is_publication=True,
            owner=self.user
        )

    def test_get_list(self):
        """Тест получения списка привычек"""

        Habit.objects.create(
            owner=self.user,
            place="test3",
            time="10:00:00",
            action="test5",
            is_pleasant=True,
            frequency=1,
            execution_time="00:02:00",
        )

        response = self.client.get('/habit/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_create(self):
        """Тест создания привычек"""

        response = self.client.post('/habit/create/',
                                    {
                                        "pk": 1,
                                        "place": "home",
                                        "time": "12:00:00",
                                        "action": "run",
                                        "is_pleasant": True,
                                        "frequency": 1,
                                        "execution_time": "00:02:00",
                                        "is_publication": True,
                                        "owner": 1

                                    })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_public_habit(self):
        """ Тестирование вывода списка привычек c флагом публикации """

        response = self.client.get('/habit/public/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_retrieve_habit(self):
        """Тестирование вывода одной привычки """

        response = self.client.get(f'/habit/{self.habit.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_put_habit(self):
        """" Тестирование patch обновление привычки"""

        data = {
            'owner': self.user.pk,
            'place': 'test',
            'time': '01:00:00',
            'action': 'test',
            'frequency': 1,
            'execution_time': "00:02:00"
        }

        response = self.client.patch(f'/habit/update/{self.habit.pk}/',
                                     data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["place"], 'test')

    def test_destroy_habit(self):
        """ Тестирование удаления привычки """

        response = self.client.delete(f'/habit/delete/{self.habit.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.all().exists())
        self.assertEqual(Habit.objects.all().count(), 0)
