Feature: Network Manager
    A site to manage the Network

    Scenario: Check the Index page
      Given a Flask application configured for testing
      When the '/' page is requested (GET)
      Then check that the response returns index

    Scenario: Check the Processes  page
      Given a Flask application configured for testing
      When the '/processes' page is requested (GET)
      Then check that the response returns processes
