import requests
from typing import Dict, Any

class ParagonService:
    def __init__(self, id_token: str):
        self.url = "https://10.117.43.137/traffic-engineering/api/topology/v2/1"
        self.headers = self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://10.117.43.137/nstopo/topology',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-iam-token': id_token  # Token de autenticación obtenido de AuthService
        }
        self.cookies = {'io': '1utAlDsnq_5V3nVdAABI'}
    def get_topology(self) -> Dict[str, Any]:

        try:
            response = requests.get(
                self.url,
                headers=self.headers,
                cookies=self.cookies,
                verify=False  # Usar --insecure en curl equivale a verify=False
            )
            response.raise_for_status()  # Lanza excepción si hay error HTTP
            return response.json()  # Retorna los datos como diccionario
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch topology: {str(e)}")

