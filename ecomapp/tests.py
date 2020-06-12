# -*- coding: utf-8 -*-
from django.test import TestCase
from .forms import LoginForm
from django.contrib.auth.models import User


# Create your tests here.
class LoginFormTest(TestCase):
    """Class for testing LoginForm form.
    """

    def test_login_form_false(self):
        data = {'username': "qwe",
                'password': "qwe"
                }
        form = LoginForm(data)

        self.assertFalse(form.is_valid())

    def test_login_form_success(self):
        User.objects.create(username="qaz", password="qaz")
        data = {'username': "qaz",
                'password': "qaz"
                }
        form = LoginForm(data)
        print(form.errors.as_data())
        self.assertTrue(form.is_valid())
