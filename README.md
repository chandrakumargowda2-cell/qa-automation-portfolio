# QA Automation Portfolio — Python, Playwright, Pytest & API Testing

Independent portfolio framework targeting [Automation Exercise](https://automationexercise.com/), a public e-commerce practice site with published [UI test cases](https://automationexercise.com/test_cases) and [API scenarios](https://automationexercise.com/api_list).

> Not affiliated with the demo site. No client code, customer data, credentials or proprietary assets are included.

## Skills demonstrated
- Python + Playwright (sync API), Pytest fixtures and Page Object Model
- UI smoke, regression and negative scenarios
- API automation with Requests: GET/POST, JSON and API business-response assertions
- Environment configuration, Faker test inputs, logging
- Unique timestamped HTML reports; failure screenshots and Playwright traces
- GitHub Actions CI for separate API and UI jobs

## Structure
```text
qa-automation-portfolio/
├── .github/workflows/tests.yml
├── api/api_client.py          # reusable Requests client
├── config/settings.py         # environment configuration
├── pages/                     # Page Object Model
├── tests/ui/                  # browser tests
├── tests/api/                 # REST API tests
├── utils/                     # test data and logging
├── test_data/                 # synthetic data guidance
├── conftest.py                # fixtures, reports, failure evidence
├── pytest.ini
├── requirements.txt
└── .env.example
```

## Setup
Python 3.10+ recommended.
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```
Copy `.env.example` to `.env` to override defaults. Never commit secrets.

## Run
```bash
pytest                  # all tests
pytest -m ui -v         # UI suite
pytest -m api -v        # API suite
HEADLESS=false pytest -m ui -v
BROWSER=firefox pytest -m ui -v  # after playwright install firefox
```

## Included coverage
| Layer | Scenario |
|---|---|
| UI | Home page loads |
| UI | Product catalogue visible |
| UI | Search products |
| UI | Invalid login rejected |
| API | GET products and validate collection |
| API | GET brands and validate collection |
| API | Search products |
| API | Search without required parameter |
| API | Unsupported POST method |
| API | Invalid login / missing credentials |

The demo API may return HTTP 200 while placing the business result in JSON `responseCode`; tests validate both transport and API-level responses. Public demo services can change or be temporarily unavailable; re-check current behavior if a live test fails.

## Reports and debugging
Each run creates a microsecond-stamped unique report in `reports/`, preventing same-second runs from overwriting one another. Failed UI tests attempt to save screenshots in `screenshots/` and traces in `traces/`. Open a trace with `playwright show-trace path/to/trace.zip`.

## Responsible use
Run a reasonable number of tests; do not load-test the public site. Use synthetic data only. Account creation/deletion APIs are excluded from the default suite because they mutate remote records. Generated reports, screenshots, traces and logs are ignored by Git; commit only sanitized evidence.

## Author
**Chandrakumar T S** — QA Automation | Python | Playwright | Pytest | API Testing

Add your LinkedIn and GitHub profile URLs here before publishing.

## Suggested extensions
Allure, accessibility checks, visual regression, contract/schema validation, cross-browser CI, database validation against a suitable demo backend, and historical test reporting.
