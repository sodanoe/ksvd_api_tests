import pytest

from src.http_client import HttpClient


@pytest.fixture
def http_client(config):
    return HttpClient(config['app_url'])
