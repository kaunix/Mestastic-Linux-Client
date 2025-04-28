"""
Settings Window

Provides an interface for user-configurable settings.
"""

from PyQt6 import QtWidgets

class SettingsWindow(QtWidgets.QWidget):
    """Window for application settings."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.resize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        """Set up settings panel."""
        layout = QtWidgets.QVBoxLayout()
        self.dark_mode_toggle = QtWidgets.QCheckBox("Enable Dark Mode")
        layout.addWidget(self.dark_mode_toggle)
        self.setLayout(layout)

