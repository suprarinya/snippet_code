from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage, QWebEngineSettings
from PyQt5.QtWidgets import QApplication
import time

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    webview = QWebEngineView()
    profile = QWebEngineProfile("my_profile", webview)
    profile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
    webpage = QWebEnginePage(profile, webview)
    webpage.settings().setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)

    webview.setPage(webpage)
    webview.load(QUrl("https://www.youtube.com/watch?v=aKCNrkERJ3E"))
    webview.show()

    sys.exit(app.exec_())