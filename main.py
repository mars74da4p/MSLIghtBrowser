import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class BrowserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MSLightBrowser")
        self.resize(1280, 820)

        self.home_url = "https://example.com"

        self.back_btn = QPushButton("←")
        self.forward_btn = QPushButton("→")
        self.reload_btn = QPushButton("↻")
        self.home_btn = QPushButton("Home")
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.home_url))
        self.browser.urlChanged.connect(self.update_address_bar)

        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)
        self.home_btn.clicked.connect(self.go_home)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.back_btn)
        nav_layout.addWidget(self.forward_btn)
        nav_layout.addWidget(self.reload_btn)
        nav_layout.addWidget(self.home_btn)
        nav_layout.addWidget(self.address_bar)

        main_layout = QVBoxLayout()
        main_layout.addLayout(nav_layout)
        main_layout.addWidget(self.browser)
        self.setLayout(main_layout)

    def load_url(self):
        raw = self.address_bar.text().strip()
        if not raw:
            return

        if "://" not in raw:
            raw = "https://" + raw

        try:
            self.browser.setUrl(QUrl(raw))
        except Exception:
            self.browser.setUrl(QUrl("https://example.com"))

    def update_address_bar(self, url):
        self.address_bar.setText(url.toString())

    def go_home(self):
        self.browser.setUrl(QUrl(self.home_url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
