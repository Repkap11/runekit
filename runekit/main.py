import logging
import signal
import sys
import traceback

import click
from PySide6.QtCore import QSettings, Qt, QTimer
from PySide6.QtWidgets import (
    QApplication,
    QMessageBox,
)

import runekit._resources
from runekit import browser
from runekit.game import get_platform_manager
from runekit.host import Host
import time


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.option("--game-index", default=0, help="Game instance index, starting from 0")
@click.argument("qt_args", nargs=-1, type=click.UNPROCESSED)
@click.argument("app_url", required=False)
def main(app_url, game_index, qt_args):
    print("Paul startting main")
    print("Paul creating app")
    app = QApplication(["runekit", *qt_args])
    print("Paul app created")
    # time.sleep(5)


    logging.basicConfig(level=logging.DEBUG)

    logging.info("Starting QtWebEngine")
    browser.init()
    print("Paul here 1")


    app.setQuitOnLastWindowClosed(False)
    app.setOrganizationName("cupco.de")
    app.setOrganizationDomain("cupco.de")
    app.setApplicationName("RuneKit")
    print("Paul here 5")


    signal.signal(signal.SIGINT, lambda no, frame: app.quit())

    timer = QTimer()
    timer.start(300)
    timer.timeout.connect(lambda: None)

    QSettings.setDefaultFormat(QSettings.IniFormat)
    print("Paul here 8")

    try:
        game_manager = get_platform_manager()
        print("Paul here 8")
        host = Host(game_manager)

        if app_url == "settings":
            host.open_settings()
            host.setting_dialog.setAttribute(Qt.WA_DeleteOnClose)
            host.setting_dialog.destroyed.connect(app.quit)
        elif app_url:
            logging.info("Loading app")
            game_app = host.launch_app_from_url(app_url)
            game_app.window.destroyed.connect(app.quit)
        else:
            logging.info("Loading Clue by default")
            # game_app = host.launch_app_from_url("https://runeapps.org/apps/clue/appconfig.json")
            game_app = host.launch_app_from_url("https://cluetrainer.app/appconfig.json")
            # game_app.window.destroyed.connect(app.quit)
            # if not host.app_store.has_default_apps():
                # host.app_store.load_default_apps()

        print("Paul here 10")
        app.exec_()
        sys.exit(0)
    except Exception as e:
        msg = QMessageBox(
            QMessageBox.Critical,
            "Oh No!",
            f"Fatal error: \n\n{e.__class__.__name__}: {e}",
        )
        msg.setDetailedText(traceback.format_exc())
        msg.exec_()

        raise
    finally:
        if game_manager is not None:
            logging.debug("Stopping game manager")
            game_manager.stop()


if __name__ == "__main__":
    main()
