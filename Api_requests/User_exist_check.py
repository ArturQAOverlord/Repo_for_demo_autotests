import requests

url = "https://demoqa.ru/Account/v1/User/"

def User_exist_check(uuid, token):
  user_url = url+str(uuid)
  payload = {}
  headers = {
    'accept': 'application/json',
    'Authorization': f"Bearer {token}"
  }

  response = requests.request("GET", user_url, headers=headers, data=payload)

  assert response.status_code == 200, f'Пользователь не нашелся, {response.status_code}'