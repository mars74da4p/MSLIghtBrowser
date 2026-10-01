from PyQt5.QtCore import Qt, QUrl, QSize
from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
    QTabWidget,
    QMenu,
    QAction,
    QMessageBox,
    QComboBox,
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

from tab_widget import BrowserTab
from dark_theme import apply_dark_theme, apply_light_theme
from privacy import PrivacyManager
from settings import SettingsDialog


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MSLightBrowser")
        self.setGeometry(100, 100, 1280, 820)
        
        self.privacy_manager = PrivacyManager()
        self.dark_mode = False
        self.ad_blocking_enabled = True
        self.home_url = "https://duckduckgo.com"
        
        self.init_ui()
        self.apply_theme()
        
    def init_ui(self):
        """Инициализация пользовательского интерфейса"""
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Верхняя панель навигации
        nav_layout = QHBoxLayout()
        
        self.back_btn = QPushButton("←")
        self.forward_btn = QPushButton("→")
        self.reload_btn = QPushButton("↻")
        self.home_btn = QPushButton("⌂")
        
        self.back_btn.clicked.connect(self.go_back)
        self.forward_btn.clicked.connect(self.go_forward)
        self.reload_btn.clicked.connect(self.reload)
        self.home_btn.clicked.connect(self.go_home)
        
        for btn in [self.back_btn, self.forward_btn, self.reload_btn, self.home_btn]:
            btn.setMaximumWidth(40)
            btn.setMinimumHeight(30)
        
        nav_layout.addWidget(self.back_btn)
        nav_layout.addWidget(self.forward_btn)
        nav_layout.addWidget(self.reload_btn)
        nav_layout.addWidget(self.home_btn)
        
        # Комбо-бокс для выбора поисковика
        self.search_engine_combo = QComboBox()
        self.search_engine_combo.addItem("DuckDuckGo", "https://duckduckgo.com/?q=")
        self.search_engine_combo.addItem("Google", "https://www.google.com/search?q=")
        self.search_engine_combo.addItem("Yandex", "https://yandex.ru/search/?text=")
        self.search_engine_combo.addItem("Bing", "https://www.bing.com/search?q=")
        self.search_engine_combo.setMaximumWidth(100)
        nav_layout.addWidget(self.search_engine_combo)
        
        # Адресная строка / поисковая строка
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Search or enter URL...")
        self.address_bar.returnPressed.connect(self.load_url)
        nav_layout.addWidget(self.address_bar)
        
        # Кнопка меню
        self.menu_btn = QPushButton("≡")
        self.menu_btn.clicked.connect(self.show_menu)
        self.menu_btn.setMaximumWidth(40)
        self.menu_btn.setMinimumHeight(30)
        nav_layout.addWidget(self.menu_btn)
        
        # Вкладки
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        
        # Добавляем первую вкладку
        self.add_new_tab()
        
        main_layout.addLayout(nav_layout)
        main_layout.addWidget(self.tab_widget)
        
        # Горячие клавиши
        self.setup_shortcuts()
        
    def setup_shortcuts(self):
        """Установка горячих клавиш"""
        # Ctrl+T — новая вкладка
        new_tab_shortcut = self.createAction("New Tab", self.add_new_tab, QKeySequence.New)
        
        # Ctrl+W — закрыть вкладку
        close_tab_shortcut = self.createAction("Close Tab", self.close_current_tab, QKeySequence.Close)
        
        # Ctrl+Shift+Delete — очистка данных
        clear_shortcut = self.createAction(
            "Clear Data",
            self.show_privacy_settings,
            QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_Delete)
        )
        
    def createAction(self, name, trigger, shortcut):
        """Создание действия с горячей клавишей"""
        action = QAction(name, self)
        action.triggered.connect(trigger)
        action.setShortcut(shortcut)
        self.addAction(action)
        return action
    
    def add_new_tab(self):
        """Добавить новую вкладку"""
        tab = BrowserTab(self.ad_blocking_enabled)
        tab.url_changed.connect(self.update_address_bar)
        self.tab_widget.addTab(tab, "New Tab")
        self.tab_widget.setCurrentWidget(tab)
    
    def close_tab(self, index):
        """Закрыть вкладку по индексу"""
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)
        else:
            # Если это последняя вкладка, добавляем новую перед закрытием
            self.add_new_tab()
            self.tab_widget.removeTab(0)
    
    def close_current_tab(self):
        """Закрыть текущую вкладку"""
        self.close_tab(self.tab_widget.currentIndex())
    
    def on_tab_changed(self):
        """При смене вкладки обновляем адресную строку"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab:
            self.update_address_bar(current_tab.url())
    
    def update_address_bar(self, url):
        """Обновить адресную строку"""
        if isinstance(url, QUrl):
            self.address_bar.setText(url.toString())
        else:
            self.address_bar.setText(str(url))
    
    def load_url(self):
        """Загрузить URL или выполнить поиск"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab:
            query = self.address_bar.text().strip()
            if not query:
                return
            
            # Проверяем, это URL или поисковый запрос
            if self.is_url(query):
                # Это URL
                if "://" not in query:
                    url = "https://" + query
                else:
                    url = query
            else:
                # Это поисковый запрос
                search_engine_url = self.search_engine_combo.currentData()
                # Кодируем пробелы и спецсимволы
                query_encoded = query.replace(" ", "+")
                url = search_engine_url + query_encoded
            
            current_tab.load_url(QUrl(url))
    
    def is_url(self, text):
        """Проверить, является ли текст URL"""
        # Простая эвристика
        url_indicators = [
            "://",
            ".",
            "localhost",
            "http",
            "ftp",
        ]
        return any(indicator in text for indicator in url_indicators)
    
    def go_back(self):
        """Назад"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab:
            current_tab.back()
    
    def go_forward(self):
        """Вперед"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab:
            current_tab.forward()
    
    def reload(self):
        """Обновить страницу"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab:
            current_tab.reload()
    
    def go_home(self):
        """На домашнюю страницу (DuckDuckGo)"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab:
            current_tab.load_url(QUrl(self.home_url))
    
    def show_menu(self):
        """Показать главное меню"""
        menu = QMenu(self)
        
        new_tab_action = menu.addAction("New Tab")
        new_tab_action.triggered.connect(self.add_new_tab)
        
        menu.addSeparator()
        
        dark_mode_action = menu.addAction("Toggle Dark Mode")
        dark_mode_action.triggered.connect(self.toggle_dark_mode)
        
        privacy_action = menu.addAction("Privacy Settings")
        privacy_action.triggered.connect(self.show_privacy_settings)
        
        ad_block_action = menu.addAction("Toggle Ad Blocking")
        ad_block_action.triggered.connect(self.toggle_ad_blocking)
        
        menu.addSeparator()
        
        about_action = menu.addAction("About")
        about_action.triggered.connect(self.show_about)
        
        menu.exec_(self.menu_btn.mapToGlobal(self.menu_btn.rect().bottomLeft()))
    
    def toggle_dark_mode(self):
        """Переключить тёмный режим"""
        self.dark_mode = not self.dark_mode
        self.apply_theme()
    
    def apply_theme(self):
        """Применить тему"""
        if self.dark_mode:
            apply_dark_theme(self)
        else:
            apply_light_theme(self)
    
    def show_privacy_settings(self):
        """Показать диалог приватности"""
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Privacy Settings")
        dialog.setText(
            "Clear browsing data?\n\n"
            "This will delete history, cookies, and cache.\n\n"
            "Note: This is a simplified version. Full implementation requires WebEngine profile access."
        )
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        if dialog.exec_() == QMessageBox.Yes:
            self.privacy_manager.clear_cache()
            self.privacy_manager.clear_cookies()
            self.privacy_manager.clear_history()
            QMessageBox.information(self, "Success", "Browsing data cleared!")
    
    def toggle_ad_blocking(self):
        """Переключить блокировку рекламы"""
        self.ad_blocking_enabled = not self.ad_blocking_enabled
        status = "enabled" if self.ad_blocking_enabled else "disabled"
        QMessageBox.information(
            self,
            "Ad Blocking",
            f"Ad blocking has been {status}.\nReload pages for changes to take effect."
        )
    
    def show_about(self):
        """Показать информацию о браузере"""
        QMessageBox.about(
            self,
            "About MSLightBrowser",
            "MSLightBrowser v1.0\n\n"
            "A lightweight, fast browser with modern security protocols.\n\n"
            "Features:\n"
            "• Tab support\n"
            "• Dark theme\n"
            "• Ad blocking\n"
            "• Privacy controls\n"
            "• Search via DuckDuckGo, Google, Yandex, Bing\n"
            "• TLS 1.3 support\n\n"
            "License: MIT\n\n"
            "Home: https://duckduckgo.com"
        )
