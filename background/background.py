"""Class to handle background processes"""

import sys
import threading
import time

from flask import render_template

class Background():
    """Class to handle background processes"""

    def __init__(self, app, turbo):
        """Initializer, pass in the Flask App, and the Turbo Flask"""
        self.app = app
        self.turbo = turbo
        app.context_processor(self.inject_load)

        with app.app_context():
            threading.Thread(target=self.update_load).start()

    def update_load(self):
        """Render the template"""
        with self.app.app_context():
            while True:
                time.sleep(5)
                self.turbo.push(
                    self.turbo.replace(
                        render_template('loadavg.html'),
                        'load'))

    def inject_load(self):
        """Get some data"""
        load = []
        if sys.platform.startswith('linux'):
            with open('/proc/loadavg', mode='rt' , encoding="utf-8") as f:
                load = f.read().split()[0:3]
        return {'load1': load[0], 'load5': load[1], 'load15': load[2]}
