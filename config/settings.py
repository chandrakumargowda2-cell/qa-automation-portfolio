import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com").rstrip("/")
API_BASE_URL = os.getenv("API_BASE_URL", f"{BASE_URL}/api").rstrip("/")
BROWSER = os.getenv("BROWSER", "chromium").lower()
HEADLESS = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
