import requests
import json

url = "https://demoqa.ru/Account/v1/User"

def User_creation(username, password):
  payload = json.dumps({
    "userName": username,
    "password": password
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  assert response.status_code == 201, f'Пользователь не создался, {response.status_code}'

  return response