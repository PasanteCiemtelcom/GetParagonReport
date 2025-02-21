import requests
from src.models.authResponseModel import AuthResponseModel  # Ajustado al nombre correcto

class AuthService:
    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password

        self.url = "https://10.117.43.137/iam/authenticate"
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Origin': 'https://10.117.43.137',
            'Referer': 'https://10.117.43.137/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
        }
        self.body = {
            "user": {
                "domain": "default",
                "name": user
            },
            "password": password,
            "methods": [
                "PASSWORD"
            ]
        }
        self.user_id = None
        self.id_token = None

    def login(self) -> None:
        try:
            response = requests.post(self.url, headers=self.headers, json=self.body, verify=False)
            response.raise_for_status()
            json_data = response.json()
            auth_response = AuthResponseModel.from_dict(json_data)
            self.user_id = auth_response.user_id
            self.id_token = auth_response.id_token
        except requests.exceptions.RequestException as e:
            raise Exception(f"Authentication failed: {str(e)}")
        except ValueError as e:
            raise Exception(f"Invalid JSON response: {str(e)}")
        except AssertionError as e:
            raise Exception(f"Response does not match AuthResponseModel structure: {str(e)}")