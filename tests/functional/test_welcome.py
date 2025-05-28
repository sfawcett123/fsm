from bs4 import BeautifulSoup
from pytest_bdd import (parsers, given, scenarios, then, when,)

scenarios('features/functional.feature')


@given('a Flask application configured for testing',
       target_fixture="test_client")
def _(application):
    """a Flask application configured for testing."""
    return application.test_client()


@when(parsers.parse("the '{page}' page is requested (GET)"),
      target_fixture="soup")
def _(test_client, page):
    """the '/' page is requested (GET)."""
    response = test_client.get(page)
    assert response.status_code == 200
    return BeautifulSoup(response.data, 'html.parser')


@then(parsers.parse('check that the response returns {result}'))
def _(soup, result):
    """check that the response returns index."""
    title = soup.find("meta", property="fsm:page")
    assert result in title["content"]
