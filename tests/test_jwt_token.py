from typing import Dict

from rest_framework.test import APITestCase

from authentication.views import UserCreateView
from djangorestblog.settings import API_URI_PREFIX

CREATE_USER_VIEW = API_URI_PREFIX + "/post/auth/signup/"
GET_TOKEN = API_URI_PREFIX + "/post/auth/token/"


class ApiTestCaseAuth(object):
    def set_auth_token(self, user: Dict = None):
        pass


class TestJWTToken(APITestCase):
    def setup_method(self, method):
        self.user_create_view = UserCreateView()
        self.newuser = {}
        self.newuser["username"] = "testowy"
        self.newuser["email"] = "testowy@testowy.com"
        self.newuser["password"] = "testowytestowy"

        self.token_user = {}
        self.token_user["email"] = self.newuser["email"]
        self.token_user["password"] = self.newuser["password"]

        self.bad_user = {}
        self.bad_user["email"] = "lalamido@lalamido.com"
        self.bad_user["password"] = "lalamidolalamido"

    def test_create_user(self):

        resp = self.client.post(CREATE_USER_VIEW, self.newuser, "json")
        print(resp)
        assert resp.status_code == 201

        # assert 0==1

    def test_get_token_from_signed_user(self):
        resp = self.client.post(CREATE_USER_VIEW, self.newuser, "json")
        print(resp)

        resp2 = self.client.post(GET_TOKEN, self.token_user, "json")
        print(resp2)
        assert resp2.status_code == 200
        print(resp2.data["refresh"])
        print(resp2.data["access"])
        print(resp2.data)
        assert resp2.data["refresh"] is not None
        assert resp2.data["access"] is not None

        # assert 0==1

    def test_get_token_when_no_user_return_error(self):

        resp = self.client.post(GET_TOKEN, self.bad_user, "json")
        assert resp.status_code == 401
        # assert 0==1
