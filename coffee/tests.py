from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Coffee

from django.urls import reverse

class ThingTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_coffee = Coffee.objects.create(
            title="rake",
            purchaser=testuser1,
            price="2.5",
            reviewer="reviewr test"
        )
        test_coffee.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_coffee_model(self):
        coffee = Coffee.objects.get(id=1)
        actual_title = str(coffee.title)
        actual_purchaser = str(coffee.purchaser)
        actual_price = str(coffee.price)
        actual_reviewer = str(coffee.reviewer)
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_title, "rake")
        self.assertEqual(actual_price, "2.5")
        self.assertEqual(actual_reviewer, "reviewr test")

    def test_get_coffee_list(self):
        url = reverse("coffee_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        coffee = response.data
        self.assertEqual(len(coffee), 1)
        

    # def test_auth_required(self):
    #     self.client.logout()
    #     url = reverse("coffee_list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("coffee_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)