from django.test import TestCase
from velocichapter.views import *
from django.core.handlers.base import BaseHandler
from django.test.client import RequestFactory
from django.contrib.auth.models import User
import mock
import sys

class RegistrationTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='fake_user', password='fake_pswd')

    def test_user_login(self):
        """mock_request = mock.Mock()
        mock_request.user = mock.Mock()
        mock_request.is_superuser = mock.Mock()
        mock_request.user.is_superuser.return_value = True
        mock_request.session = {}
        mock_request.META = {}"""

        mock_request = self.factory.post('/login')
        mock_request.user = self.user
        #mock_request.method = 'POST'
        response = user_login(mock_request)
        print >> sys.stderr, mock_request
        #self.assertEqual(response.status_code, 200)
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertEqual(user_login(request), True)


