from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Otter


class OtterTests(APITestCase):
    # In Python, the @classmethod decorator is used to declare a method in the class as a class method that can be called using ClassName.MethodName()
    # click the blue circle, this overrides a particular method
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_thing = Otter.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_thing.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")


    def test_otters_model(self):
        otter = Otter.objects.get(id=1)
        actual_owner = str(otter.owner)
        actual_name = str(otter.name)
        actual_description = str(otter.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_otter_list(self):
        url = reverse("otter_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        otters = response.data
        self.assertEqual(len(otters), 1)
        self.assertEqual(otters[0]["name"], "rake")

    def test_get_thing_by_id(self):
        url = reverse("otter_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        otter = response.data
        self.assertEqual(otter["name"], "rake")

    def test_create_thing(self):
        url = reverse("otter_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        otters = Otter.objects.all()
        self.assertEqual(len(otters), 2)
        self.assertEqual(Otter.objects.get(id=2).name, "spoon")

    def test_update_thing(self):
        url = reverse("otter_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        otter = Otter.objects.get(id=1)
        self.assertEqual(otter.name, data["name"])
        self.assertEqual(otter.owner.id, data["owner"])
        self.assertEqual(otter.description, data["description"])

    def test_delete_thing(self):
        url = reverse("otter_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        otters = Otter.objects.all()
        self.assertEqual(len(otters), 0)

        # New

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("otter_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
