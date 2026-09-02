import pytest

from Api_requests.User_creation import User_creation
from Api_requests.User_deletion import User_deletion
from Api_requests.User_exist_check import User_exist_check
from Api_requests.User_token_gen import User_token_gen

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "slow_mo": 300,
    }


@pytest.fixture
def user():
    username = "test_user_1231f5154asasfaff41"
    password = "Test1234!"

    response = User_creation(username, password)
    user_id = response.json()["userId"]

    token = User_token_gen(username, password).json()['token']
    User_exist_check(user_id, token)

    yield {
        "username": username,
        "password": password,
        "user_id": user_id
    }

    User_deletion(user_id, token)