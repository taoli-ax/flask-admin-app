from .admin import admin_cli
from flask import Flask


def init_scripts(app: Flask):
    app.cli.add_command(admin_cli)


