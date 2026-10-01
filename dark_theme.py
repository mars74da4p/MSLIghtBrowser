def apply_dark_theme(window):
    """Применить тёмную тему к окну браузера"""
    dark_stylesheet = """
    QMainWindow {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    QWidget {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    QPushButton {
        background-color: #333333;
        color: #ffffff;
        border: 1px solid #555555;
        border-radius: 4px;
        padding: 4px;
    }
    QPushButton:hover {
        background-color: #444444;
    }
    QPushButton:pressed {
        background-color: #252525;
    }
    QLineEdit {
        background-color: #333333;
        color: #ffffff;
        border: 1px solid #555555;
        border-radius: 4px;
        padding: 4px;
    }
    QLineEdit:focus {
        border: 1px solid #0d47a1;
    }
    QTabWidget::pane {
        border: 1px solid #555555;
    }
    QTabBar::tab {
        background-color: #333333;
        color: #ffffff;
        border: 1px solid #555555;
        padding: 4px 8px;
        margin: 2px;
    }
    QTabBar::tab:selected {
        background-color: #444444;
        border-bottom: 2px solid #0d47a1;
    }
    QTabBar::close-button {
        background-color: transparent;
    }
    QMenu {
        background-color: #333333;
        color: #ffffff;
        border: 1px solid #555555;
    }
    QMenu::item:selected {
        background-color: #0d47a1;
    }
    QMessageBox {
        background-color: #1e1e1e;
    }
    QMessageBox QLabel {
        color: #ffffff;
    }
    QMessageBox QPushButton {
        min-width: 60px;
    }
    """
    window.setStyleSheet(dark_stylesheet)


def apply_light_theme(window):
    """Применить светлую тему к окну браузера"""
    light_stylesheet = """
    QMainWindow {
        background-color: #ffffff;
        color: #000000;
    }
    QWidget {
        background-color: #ffffff;
        color: #000000;
    }
    QPushButton {
        background-color: #f0f0f0;
        color: #000000;
        border: 1px solid #cccccc;
        border-radius: 4px;
        padding: 4px;
    }
    QPushButton:hover {
        background-color: #e0e0e0;
    }
    QPushButton:pressed {
        background-color: #ffffff;
    }
    QLineEdit {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #cccccc;
        border-radius: 4px;
        padding: 4px;
    }
    QLineEdit:focus {
        border: 1px solid #0d47a1;
    }
    QTabWidget::pane {
        border: 1px solid #cccccc;
    }
    QTabBar::tab {
        background-color: #f0f0f0;
        color: #000000;
        border: 1px solid #cccccc;
        padding: 4px 8px;
        margin: 2px;
    }
    QTabBar::tab:selected {
        background-color: #ffffff;
        border-bottom: 2px solid #0d47a1;
    }
    QTabBar::close-button {
        background-color: transparent;
    }
    QMenu {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #cccccc;
    }
    QMenu::item:selected {
        background-color: #0d47a1;
        color: #ffffff;
    }
    """
    window.setStyleSheet(light_stylesheet)
