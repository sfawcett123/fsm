"""Index Handler"""
from flask import render_template
from flask import current_app as app
from flask.views import View


class Index(View):

    def dispatch_request(self):
        return render_template('/index/index.html')
