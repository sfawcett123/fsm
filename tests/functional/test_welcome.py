from bs4 import BeautifulSoup
from pytest_bdd import (parsers, given, scenarios, then, when,)

scenarios('features/functional.feature')


@given('a Flask application configured for testing',
       target_fixture="test_client")
def _(application):
    """a Flask application configured for testing."""
    return application.test_client()


@when(parsers.parse("the {page} page is requested (GET)"),
      target_fixture="soup")
def _(test_client, page):
    """the '/' page is requested (GET)."""
    response = test_client.get(page.replace("'", ""))
    assert response.status_code == 200
    return BeautifulSoup(response.data, 'html.parser')


@then(parsers.parse('check that the response returns {result}'))
def _(soup, result):
    """check that the response returns index."""
    title = soup.find("meta", property="fsm:page")
    assert result == title["content"]

@then( parsers.parse( 'check the menu option {option} has link to {link}') )
def _( soup , option, link):
    """check the option has link  to link."""
    for anchor in soup.find_all( "a" ):
        if anchor.string == option:
            assert link ==  anchor["href"] 

