"""
Firmware Update Window

Allows users to upload and flash new firmware to Meshtastic devices.
"""

from PyQt6 import QtWidgets

class FirmwareUpdateWindow(QtWidgets.QWidget):
    """Window for firmware updates."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Firmware Update")
        self.resize(400, 200)
        self.setup_ui()

    def setup_ui(self):
        """Set up firmware update UI."""
        layout = QtWidgets.QVBoxLayout()
        self.choose_file_button = QtWidgets.QPushButton("Choose Firmware File")
        self.flash_button = QtWidgets.QPushButton("Flash Device")
        layout.addWidget(self.choose_file_button)
        layout.addWidget(self.flash_button)
        self.setLayout(layout)

