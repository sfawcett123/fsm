"""Index Handler"""
from flask import render_template
# from flask import current_app as app
from flask.views import View
import psutil


class Service(View):

    def show_services(self):
        return [(
            psutil.Process(p).name(),
            psutil.Process(p).status(),
        ) for p in psutil.pids()]

    def dispatch_request(self):
        return render_template(
            '/service/index.html',
            services=self.show_services())
