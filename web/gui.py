
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
# pip3 install PyQtWebEngine
from PyQt5.QtWebEngineWidgets import QWebEngineView
from utils import Config


def startQtGUI():
    qt_app = QApplication(sys.argv)
    web = QWebEngineView()
    web.setWindowTitle("GifGang")
    web.resize(1200, 800)
    web.setZoomFactor(1.5)
    web.load(QUrl(f"http://{Config.host}:{Config.port}/"))
    web.show()
    sys.exit(qt_app.exec_())


if __name__ == "__main__":
    startQtGUI()
