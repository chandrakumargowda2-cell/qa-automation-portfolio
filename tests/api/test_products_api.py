import pytest

def payload_of(response):
    response.raise_for_status()
    try: return response.json()
    except ValueError: pytest.fail(f"Expected JSON; got {response.text[:250]}")

@pytest.mark.api
@pytest.mark.smoke
def test_get_all_products_returns_collection(api_client):
    data = payload_of(api_client.get("productsList"))
    assert data.get("responseCode") == 200
    assert isinstance(data.get("products"), list) and data["products"]
    for key in ("id", "name", "price", "brand", "category"): assert key in data["products"][0]

@pytest.mark.api
@pytest.mark.smoke
def test_get_all_brands_returns_collection(api_client):
    data = payload_of(api_client.get("brandsList"))
    assert data.get("responseCode") == 200
    assert isinstance(data.get("brands"), list) and data["brands"]

@pytest.mark.api
def test_search_products_with_keyword(api_client):
    data = payload_of(api_client.post("searchProduct", data={"search_product": "top"}))
    assert data.get("responseCode") == 200
    assert isinstance(data.get("products"), list) and data["products"]

@pytest.mark.api
@pytest.mark.negative
def test_search_products_without_parameter(api_client):
    data = payload_of(api_client.post("searchProduct", data={}))
    assert data.get("responseCode") == 400
    assert "missing" in data.get("message", "").lower()

@pytest.mark.api
@pytest.mark.negative
def test_post_to_products_list_is_not_supported(api_client):
    data = payload_of(api_client.post("productsList", data={}))
    assert data.get("responseCode") == 405
    assert "not supported" in data.get("message", "").lower()
