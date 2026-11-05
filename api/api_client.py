import requests
from config.settings import API_BASE_URL
class ApiClient:
    def __init__(self, base_url=API_BASE_URL, timeout=20):
        self.base_url = base_url.rstrip("/"); self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
    def get(self, endpoint, **kwargs):
        return self.session.get(f"{self.base_url}/{endpoint.lstrip('/')}", timeout=self.timeout, **kwargs)
    def post(self, endpoint, **kwargs):
        return self.session.post(f"{self.base_url}/{endpoint.lstrip('/')}", timeout=self.timeout, **kwargs)
    def close(self): self.session.close()
