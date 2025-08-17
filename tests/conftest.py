import pytest


@pytest.fixture
def test_data():
    return [
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.024,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-23T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.02,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:57:34+00:00",
            "status": 200,
            "url": "/api/specializations/...",
            "request_method": "GET",
            "response_time": 0.044,
            "http_user_agent": "...",
        },
    ]


@pytest.fixture
def wrong_test_data():
    return [
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.024,
            "http_user_agent": "...",
        },
        "invalid json",
        {
            "@timestamp": "2025-06-22T13:57:34+00:00",
            "status": 200,
            "url": "/api/specializations/...",
            "request_method": "GET",
            "response_time": 0.044,
            "http_user_agent": "...",
        },
    ]


@pytest.fixture
def test_data_for_report():
    return [
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.024,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-23T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.02,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:57:34+00:00",
            "status": 200,
            "url": "/api/specializations/...",
            "request_method": "GET",
            "response_time": 0.044,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:59:28+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.04,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:59:04+00:00",
            "status": 200,
            "url": "/api/homeworks/...",
            "request_method": "GET",
            "response_time": 0.168,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:59:29+00:00",
            "status": 200,
            "url": "/api/homeworks/...",
            "request_method": "GET",
            "response_time": 0.056,
            "http_user_agent": "...",
        },
    ]


@pytest.fixture
def wrong_test_data_for_report():
    return [
        {
            "@timestamp": "2025-06-22T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.024,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-23T13:57:32+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "response_time": 0.02,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:57:34+00:00",
            "status": 200,
            "request_method": "GET",
            "response_time": 0.044,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:59:28+00:00",
            "status": 200,
            "url": "/api/context/...",
            "request_method": "GET",
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:59:04+00:00",
            "status": 200,
            "url": "/api/homeworks/...",
            "request_method": "GET",
            "response_time": 0.168,
            "http_user_agent": "...",
        },
        {
            "@timestamp": "2025-06-22T13:59:29+00:00",
            "status": 200,
            "url": "/api/homeworks/...",
            "request_method": "GET",
            "response_time": 0.056,
            "http_user_agent": "...",
        },
    ]
