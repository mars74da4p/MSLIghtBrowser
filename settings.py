from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QCheckBox,
    QPushButton,
    QGroupBox,
)


class SettingsDialog(QDialog):
    """Диалог настроек браузера"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setGeometry(300, 300, 400, 300)
        
        layout = QVBoxLayout()
        
        # Группа приватности
        privacy_group = QGroupBox("Privacy")
        privacy_layout = QVBoxLayout()
        
        self.history_checkbox = QCheckBox("Save browsing history")
        self.history_checkbox.setChecked(True)
        privacy_layout.addWidget(self.history_checkbox)
        
        self.cookies_checkbox = QCheckBox("Allow cookies")
        self.cookies_checkbox.setChecked(True)
        privacy_layout.addWidget(self.cookies_checkbox)
        
        self.js_checkbox = QCheckBox("Allow JavaScript")
        self.js_checkbox.setChecked(True)
        privacy_layout.addWidget(self.js_checkbox)
        
        privacy_group.setLayout(privacy_layout)
        layout.addWidget(privacy_group)
        
        # Группа внешнего вида
        appearance_group = QGroupBox("Appearance")
        appearance_layout = QVBoxLayout()
        
        self.dark_mode_checkbox = QCheckBox("Dark mode")
        self.dark_mode_checkbox.setChecked(False)
        appearance_layout.addWidget(self.dark_mode_checkbox)
        
        appearance_group.setLayout(appearance_layout)
        layout.addWidget(appearance_group)
        
        # Группа безопасности
        security_group = QGroupBox("Security")
        security_layout = QVBoxLayout()
        
        self.ad_block_checkbox = QCheckBox("Enable ad blocking")
        self.ad_block_checkbox.setChecked(True)
        security_layout.addWidget(self.ad_block_checkbox)
        
        security_group.setLayout(security_layout)
        layout.addWidget(security_group)
        
        # Кнопки
        button_layout = QHBoxLayout()
        
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        button_layout.addWidget(ok_button)
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
