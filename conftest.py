import pytest
import os

from dotenv import load_dotenv
from src.http_client import HttpClient, HttpMethods

load_dotenv()


@pytest.fixture(scope="session")
def config():
    app_url = os.getenv("APP_URL")
    if not app_url:
        raise EnvironmentError(
            f"The required environment variable '{app_url}' is missing."
        )
    return {"app_url": f"http://{app_url}", "ws": f"ws://{app_url}"}


@pytest.fixture
def http_client(config):
    return HttpClient(config["app_url"])
