"""Start Flask Application"""
import os
import yaml

from flask import Flask
from turbo_flask import Turbo

from views.index import Index
from views.map import Map
from background.background import Background

app = Flask(__name__)
turbo = Turbo(app)
bg = Background(app, turbo)

CONFIG = "config.yml"

if os.path.isfile(CONFIG):
    with open(CONFIG, mode='r' , encoding="utf-8") as file:
        data = yaml.safe_load(file)
    app.config.from_object(data)

app.add_url_rule("/", view_func=Index.as_view("index"))
app.add_url_rule("/map", view_func=Map.as_view("map", app))

app.config["APPLICATION_NAME"] = data.get(
    "APPLICATION_NAME", f"Set APPLICATION_NAME in {CONFIG}")

if __name__ == "__main__":
    app.run()
