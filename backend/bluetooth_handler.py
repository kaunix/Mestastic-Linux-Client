"""
Bluetooth Handler

Handles Bluetooth scanning and connecting to Meshtastic devices.
"""

import asyncio
import bleak
import meshtastic.ble_interface

class BluetoothHandler:
    """Handles scanning for Bluetooth devices and connecting."""

    def __init__(self):
        self.interface = None

    def scan_for_devices(self):
        """
        Scan for nearby Bluetooth Meshtastic devices.

        Returns:
            dict: Mapping of device names to MAC addresses
        """
        devices = {}
        scanner = bleak.BleakScanner()
        found = asyncio.run(scanner.discover(timeout=5))
        for d in found:
            if "Meshtastic" in d.name:
                devices[d.name] = d.address
        return devices

    def connect(self, address):
        """
        Connect to a Bluetooth device by MAC address.

        Args:
            address (str): Bluetooth MAC address
        """
        self.interface = meshtastic.ble_interface.BLEInterface(devPath=address)
        asyncio.run(self.interface.connect())

    def disconnect(self):
        """Disconnect the current Bluetooth session."""
        if self.interface:
            asyncio.run(self.interface.close())
            self.interface = None

