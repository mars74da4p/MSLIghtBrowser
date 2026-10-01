from PyQt5.QtCore import QUrl


class AdBlocker:
    """Простой блокировщик рекламы на основе чёрного списка доменов"""
    
    # Популярные рекламные домены
    BLOCKED_DOMAINS = {
        # Google Ads
        "ads.google.com",
        "pagead2.googlesyndication.com",
        "googleadservices.com",
        "google-analytics.com",
        "analytics.google.com",
        
        # Facebook Ads
        "facebook.com/ads",
        "connect.facebook.net",
        
        # Yandex Ads
        "yandex.ru/ads",
        "an.yandex.ru",
        "adfox.ru",
        
        # Other ads
        "doubleclick.net",
        "ad-delivery.ru",
        "doubleclick.com",
        "advertising.com",
        "adscale.de",
        "adnxs.com",
        "criteo.com",
        "outbrain.com",
        "taboola.com",
        "scorecardresearch.com",
        "adsymptotic.com",
    }
    
    def __init__(self):
        self.blocked_count = 0
    
    def is_ad_url(self, url):
        """Проверить, является ли URL рекламным"""
        if isinstance(url, QUrl):
            host = url.host()
        else:
            host = str(url)
        
        # Проверяем точное совпадение и частичное совпадение
        for blocked_domain in self.BLOCKED_DOMAINS:
            if host == blocked_domain or host.endswith("." + blocked_domain):
                self.blocked_count += 1
                return True
        
        return False
    
    def get_blocked_count(self):
        """Получить количество заблокированных объявлений"""
        return self.blocked_count
    
    def reset_count(self):
        """Сбросить счётчик"""
        self.blocked_count = 0
