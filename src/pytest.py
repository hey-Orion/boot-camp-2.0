@pytest.mark.perametrize(
    "events,expected",
    [
        ([{"event_type": "click", "is_valid": True}], {"click": 1}),
        ([], {}),
    ]
)
def test_process_user_events_parametrized(events, expected):
    assert process_user_events(events) == expected

def test_amount_validation_rejects_negative():
    with pytest.raises(ValueError):
        Transaction(amount=-5)

from unittest.mock import patch

def test_fetch_data_handles_api_call():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": "ok"}
        mock_get.return_value.raise_for_status.return_value = None

        response = requests.get("https://api.example.com/v1/data")

        assert response.json() == {"result": "ok"}