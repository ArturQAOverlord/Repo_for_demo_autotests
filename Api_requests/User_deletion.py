import requests

url = "https://demoqa.ru/Account/v1/User/"

def User_deletion(uuid, token):
  user_url = url + str(uuid)
  payload = {}
  headers = {
    'accept': 'application/json',
    'Authorization': f"Bearer {token}"
  }

  response = requests.request("DELETE", user_url, headers=headers, data=payload)

  assert response.status_code == 200, f'Пользователь не был удален, {response.status_code}'