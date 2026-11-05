import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL",
    "https://automationexercise.com"
)

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    f"{BASE_URL}/api"
)

BROWSER = os.getenv("BROWSER", "chromium").lower()

# Automatically detect GitHub Actions
IS_CI = os.getenv("GITHUB_ACTIONS", "").lower() == "true"

# Force headless in CI; use .env toggle locally
HEADLESS = (
    True if IS_CI
    else os.getenv("HEADLESS", "false").lower() in ("true", "yes", "1")
)

SLOW_MO = int(os.getenv("SLOW_MO", "0"))

DEFAULT_TIMEOUT = int(
    os.getenv("DEFAULT_TIMEOUT", "10000")
)