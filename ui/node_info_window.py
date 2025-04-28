"""
Node Info Window

Displays information about the connected Meshtastic device.
"""

from PyQt6 import QtWidgets

class NodeInfoWindow(QtWidgets.QWidget):
    """Window showing node firmware, hardware info."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Node Info")
        self.resize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        """Set up node info display."""
        layout = QtWidgets.QFormLayout()
        self.firmware_label = QtWidgets.QLabel("Firmware: ---")
        self.hardware_label = QtWidgets.QLabel("Hardware: ---")
        layout.addRow("Firmware Version:", self.firmware_label)
        layout.addRow("Hardware Model:", self.hardware_label)
        self.setLayout(layout)

