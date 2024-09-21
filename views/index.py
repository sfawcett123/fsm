"""Index Handler"""
from flask import render_template
from flask.views import View


class Index(View):
    """Class to handle Index View"""
    menu_options = [{'name': 'Item 1', 'url': '/index'},
                    {'name': 'Item 2', 'url': '/index'}]

    def dispatch_request(self):
        """Render the template"""
        return render_template(
            'views/index.html',
            menu=self.menu_options,
            footer="Steven Loves Custard")
