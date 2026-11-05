import pytest
from utils.data_factory import invalid_email

@pytest.mark.api
@pytest.mark.negative
def test_verify_login_rejects_invalid_credentials(api_client):
    response = api_client.post("verifyLogin", data={"email": invalid_email(), "password": "DefinitelyWrong_123!"})
    response.raise_for_status(); data = response.json()
    assert data.get("responseCode") == 404
    assert "not found" in data.get("message", "").lower()

@pytest.mark.api
@pytest.mark.negative
def test_verify_login_requires_credentials(api_client):
    response = api_client.post("verifyLogin", data={"password": "anything"})
    response.raise_for_status(); data = response.json()
    assert data.get("responseCode") == 400
    assert "missing" in data.get("message", "").lower()
