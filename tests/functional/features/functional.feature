Feature: Network Manager
    A site to manage the Network

    Scenario Outline: Check the Processes page
      Given a Flask application configured for testing
      When the <link> page is requested (GET)
      Then check that the response returns <title>

      Examples:
        | title     | link | 
        | processes | /processes  | 
        | index     | /  | 

    Scenario Outline: Check the menu links 
      Given a Flask application configured for testing
      When the '/' page is requested (GET)
      Then check the menu option <option> has link to <link>

      Examples:
        | option    | link | 
        | HOME      |  /  | 
        | PROCESSES |  /processes  | 
