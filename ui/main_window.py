"""
Main Window

Defines the main application window, containing sidebar buttons, chat display,
device list, and chat input.
"""

from PyQt6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    """Main window for the Meshtastic Linux Client."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meshtastic Linux Client")
        self.resize(1000, 700)
        self.setup_ui()

    def setup_ui(self):
        """Configure top-level widgets."""
        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        self.chat_display = QtWidgets.QTextEdit()
        self.device_list = QtWidgets.QListWidget()
        layout.addWidget(self.chat_display)
        layout.addWidget(self.device_list)
        self.setCentralWidget(central)

