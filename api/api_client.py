
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.settings import API_BASE_URL


class ApiClient:

    def __init__(self, base_url=API_BASE_URL, timeout=20):

        # Store base URL and timeout
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        # Create a reusable HTTP session
        self.session = requests.Session()

        # Configure retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
            raise_on_status=False
        )

        # Attach retry strategy to HTTP adapter
        adapter = HTTPAdapter(max_retries=retry_strategy)

        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        # Set default request headers
        self.session.headers.update({
            "Accept": "application/json"
        })

    # GET request
    def get(self, endpoint, **kwargs):

        return self.session.get(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    # POST request
    def post(self, endpoint, **kwargs):

        return self.session.post(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    # PUT request
    def put(self, endpoint, **kwargs):

        return self.session.put(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    # PATCH request
    def patch(self, endpoint, **kwargs):

        return self.session.patch(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    # DELETE request
    def delete(self, endpoint, **kwargs):

        return self.session.delete(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    # Close API session
    def close(self):

        self.session.close()

    # Context manager entry
    def __enter__(self):

        return self

    # Context manager exit
    def __exit__(self, exc_type, exc_value, traceback):

        self.close()
