from PySide6.QtWebEngineQuick import QtWebEngineQuick

from .api import Alt1WebChannel, Alt1Api
from .profile import WebProfile
from .scheme import register as register_scheme


def init():
    QtWebEngineQuick.initialize()
    register_scheme()
