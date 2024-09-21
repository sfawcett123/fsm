"""Module to gather site map"""
from flask import render_template, url_for
from flask.views import View


class Map(View):
    """Site Map class"""

    def __init__(self, app):
        """Initializer"""
        self.app = app

    def has_no_empty_params(self, rule):
        """method to see if route is empty"""
        defaults = rule.defaults if rule.defaults is not None else ()
        arguments = rule.arguments if rule.arguments is not None else ()
        return len(defaults) >= len(arguments)

    def dispatch_request(self):
        """render template with list of routes"""
        links = []
        for rule in self.app.url_map.iter_rules():
            if "GET" in rule.methods and self.has_no_empty_params(rule):
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links.append((url, rule.endpoint))
        return render_template("views/all_links.html", links=links)
