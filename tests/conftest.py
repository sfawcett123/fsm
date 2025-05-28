import pytest
from src.manager import create_app

@pytest.fixture
def application():
    return create_app()
