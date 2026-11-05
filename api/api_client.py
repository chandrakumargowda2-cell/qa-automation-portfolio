import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.settings import API_BASE_URL


class ApiClient:

    def __init__(self, base_url=API_BASE_URL, timeout=20):

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
            raise_on_status=False
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)

        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        self.session.headers.update({
            "Accept": "application/json"
        })

    def get(self, endpoint, **kwargs):

        return self.session.get(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    def post(self, endpoint, **kwargs):

        return self.session.post(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    def close(self):

        self.session.close()