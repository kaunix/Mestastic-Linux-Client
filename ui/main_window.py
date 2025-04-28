"""
Main Window

Defines the main application window, containing sidebar buttons, chat display, device list, and chat input.
"""

from PyQt6 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow):
    """Main window for the Meshtastic Linux Client."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meshtastic Linux Client")
        self.resize(1000, 700)
        self.setup

