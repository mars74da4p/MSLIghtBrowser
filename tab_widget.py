from PyQt5.QtCore import pyqtSignal, QUrl, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

from ad_blocker import AdBlocker


class BrowserTab(QWidget):
    url_changed = pyqtSignal(QUrl)
    title_changed = pyqtSignal(str)
    
    def __init__(self, ad_blocking=True):
        super().__init__()
        self.ad_blocking = ad_blocking
        self.ad_blocker = AdBlocker() if ad_blocking else None
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.web_view = QWebEngineView()
        
        # Сигналы
        self.web_view.urlChanged.connect(self.on_url_changed)
        self.web_view.titleChanged.connect(self.on_title_changed)
        
        layout.addWidget(self.web_view)
        self.setLayout(layout)
        
        # Загружаем начальную страницу
        self.web_view.setUrl(QUrl("https://example.com"))
    
    def load_url(self, url):
        """Загрузить URL"""
        self.web_view.setUrl(url)
    
    def url(self):
        """Получить текущий URL"""
        return self.web_view.url()
    
    def back(self):
        """Назад"""
        self.web_view.back()
    
    def forward(self):
        """Вперёд"""
        self.web_view.forward()
    
    def reload(self):
        """Обновить"""
        self.web_view.reload()
    
    def on_url_changed(self, url):
        """При изменении URL"""
        self.url_changed.emit(url)
    
    def on_title_changed(self, title):
        """При изменении названия страницы"""
        self.title_changed.emit(title)
        # Обновляем название вкладки в браузере
        if hasattr(self.parent(), 'setTabText'):
            index = self.parent().indexOf(self)
            if index >= 0:
                self.parent().setTabText(index, title[:30] if title else "New Tab")
