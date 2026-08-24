"""Regression coverage for the portfolio inquiry and status API."""
import os

import requests


BASE_URL = os.environ["REACT_APP_BACKEND_URL"].rstrip("/")


def test_api_root_is_reachable():
    response = requests.get(f"{BASE_URL}/api/", timeout=15)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_inquiry_returns_success_response():
    payload = {
        "name": "TEST_Resume Reviewer",
        "email": "test.reviewer@example.com",
        "message": "TEST inquiry for portfolio regression coverage",
    }
    response = requests.post(f"{BASE_URL}/api/inquiries", json=payload, timeout=15)
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Inquiry received"


def test_inquiry_rejects_missing_required_fields():
    response = requests.post(
        f"{BASE_URL}/api/inquiries", json={"name": "TEST_missing"}, timeout=15
    )
    assert response.status_code == 422
    assert "detail" in response.json()


def test_inquiry_rejects_invalid_email_format():
    response = requests.post(
        f"{BASE_URL}/api/inquiries",
        json={
            "name": "TEST_invalid_email",
            "email": "not-an-email",
            "message": "TEST invalid email regression",
        },
        timeout=15,
    )
    assert response.status_code == 422
    assert "detail" in response.json()


def test_status_create_and_list():
    payload = {"client_name": "TEST_status_regression"}
    create_response = requests.post(f"{BASE_URL}/api/status", json=payload, timeout=15)
    assert create_response.status_code == 200
    created = create_response.json()
    assert created["client_name"] == payload["client_name"]
    assert isinstance(created["id"], str)

    list_response = requests.get(f"{BASE_URL}/api/status", timeout=15)
    assert list_response.status_code == 200
    assert any(item["id"] == created["id"] for item in list_response.json())