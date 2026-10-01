import os
from pathlib import Path
from datetime import datetime


class PrivacyManager:
    """Управление приватностью и данными браузера"""
    
    def __init__(self):
        self.home_dir = Path.home()
        self.cache_dir = self.home_dir / ".cache" / "mslightbrowser"
        self.data_dir = self.home_dir / ".local" / "share" / "mslightbrowser"
        self.history_file = self.data_dir / "history.txt"
        
        # Создаём директории, если их нет
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def add_to_history(self, url, title=""):
        """Добавить страницу в историю"""
        try:
            with open(self.history_file, "a", encoding="utf-8") as f:
                timestamp = datetime.now().isoformat()
                f.write(f"{timestamp} | {url} | {title}\n")
        except Exception as e:
            print(f"Error adding to history: {e}")
    
    def get_history(self):
        """Получить историю"""
        history = []
        try:
            if self.history_file.exists():
                with open(self.history_file, "r", encoding="utf-8") as f:
                    history = f.readlines()
        except Exception as e:
            print(f"Error reading history: {e}")
        return history
    
    def clear_history(self):
        """Очистить историю"""
        try:
            if self.history_file.exists():
                self.history_file.unlink()
        except Exception as e:
            print(f"Error clearing history: {e}")
    
    def clear_cache(self):
        """Очистить кеш"""
        try:
            if self.cache_dir.exists():
                for file in self.cache_dir.iterdir():
                    if file.is_file():
                        file.unlink()
                    elif file.is_dir():
                        self._remove_dir_recursive(file)
        except Exception as e:
            print(f"Error clearing cache: {e}")
    
    def clear_cookies(self):
        """Очистить cookies"""
        # QtWebEngine управляет cookies автоматически
        # Это заглушка для интерфейса
        try:
            cookies_dir = self.data_dir / "cookies"
            if cookies_dir.exists():
                self._remove_dir_recursive(cookies_dir)
        except Exception as e:
            print(f"Error clearing cookies: {e}")
    
    def _remove_dir_recursive(self, path):
        """Рекурсивное удаление директории"""
        for item in path.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                self._remove_dir_recursive(item)
        path.rmdir()
